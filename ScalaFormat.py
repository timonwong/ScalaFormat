# -*- coding: utf-8 -*-

import sublime
import sublime_plugin

import json
import locale
import os
import re
import subprocess
import sys

PY3K = sys.version_info >= (3, 0, 0)

if PY3K:
    from .ScalaFormatLib.MergeUtils import merge_code
    from .ScalaFormatLib import log
else:
    from ScalaFormatLib.MergeUtils import merge_code
    from ScalaFormatLib import log


__file__ = os.path.normpath(os.path.abspath(__file__))
__path__ = os.path.dirname(__file__)

PLUGIN_NAME = 'ScalaFormat'
LANGUAGE_RE = re.compile(r'(?<=source\.)[\w+#]+')
SETTINGS = None


with open(os.path.join(__path__, 'scalariform.json')) as fp:
    SCALARIFORM_PREFS_DEFAULT = json.load(fp)


def plugin_loaded():
    global SETTINGS
    SETTINGS = sublime.load_settings(PLUGIN_NAME + '.sublime-settings')

if not PY3K:
    plugin_loaded()


def get_setting_view(view, key, default=None):
    try:
        settings = view.settings()
        sub_key = PLUGIN_NAME
        if settings.has(sub_key):
            proj_settings = settings.get(sub_key)
            if key in proj_settings:
                return proj_settings[key]
    except:
        pass
    return SETTINGS.get(key, default)


def get_setting_for_active_view(key, default=None):
    return get_setting_view(sublime.active_window().active_view(), key, default)


def is_enabled_in_view(view):
    caret = view.sel()[0].a
    language = LANGUAGE_RE.search(view.scope_name(caret))
    if language is None:
        return False
    return language.group(0).lower() == 'scala'


class ScalaFormatCommand(sublime_plugin.TextCommand):
    def get_setting(self, key, default=None):
        return get_setting_view(self.view, key, default=default)

    def is_enabled(self):
        return is_enabled_in_view(self.view)

    def run(self, edit):
        view = self.view
        region = sublime.Region(0, view.size())
        code = view.substr(region)
        cmd = [self.get_java_executable(), '-Dfile.encoding=utf-8', '-jar',
               self.get_scalariform_executable()]
        cmd.extend(self.get_scalariform_args())
        proc = None
        try:
            proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, startupinfo=self.get_startupinfo())
            formatted_code, errinfo = proc.communicate(code.encode('utf-8'))
            formatted_code = formatted_code.decode('utf-8')

            if proc.returncode:
                sublime.status_message('Scalariform: Error')
                log.error(errinfo.strip())
            else:
                _, err = merge_code(view, edit, code, formatted_code)
                if err:
                    sublime.error_message("%s: Merge failure: '%s'" % (PLUGIN_NAME, err))
                sublime.status_message('Scalariform: Done')
        except:
            if proc and proc.poll() is None:
                proc.terminate()
            log.error('Error while executing scalariform, please check your %s settings' % PLUGIN_NAME)

    def get_startupinfo(self):
        if os.name != 'nt':
            return None
        info = subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow = subprocess.SW_HIDE
        return info

    def get_reasonable_path(self, path):
        if not PY3K and os.name == 'nt':  # On Windows, popen won't support unicode args (Python 2.x)
            if isinstance(path, unicode):
                encoding = locale.getpreferredencoding()
                return path.encode(encoding)
        return path

    def get_java_executable(self):
        return self.get_reasonable_path(self.get_setting('java_executable', default='java'))

    def get_scalariform_executable(self):
        path = self.get_setting('scalariform_jar', default=None)
        if path is None:
            path = os.path.join(__path__, 'scalariform.jar')
        return self.get_reasonable_path(path)

    def get_scalariform_args(self):
        scalariform_prefs = SCALARIFORM_PREFS_DEFAULT.copy()
        scalariform_prefs_override = self.get_setting('scalariform', default={})
        scalariform_prefs.update(scalariform_prefs_override)

        args = ['--encoding=utf-8']
        for k, v in scalariform_prefs.items():
            if k == 'encoding':
                continue
            elif k in ['alignSingleLineCaseStatements.maxArrowIndent', 'indentSpaces']:
                args.append('-{0}={1}'.format(k, v))
            else:
                sign = '+' if v else '-'
                args.append('{0}{1}'.format(sign, k))
        return args + ['--stdin', '--forceOutput', '--stdout']


class PluginEventListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        if is_enabled_in_view(view) and get_setting_for_active_view('autoformat_on_save', default=False):
            view.run_command('scala_format')

    def on_query_context(self, view, key, operator, operand, match_all):
        if key == 'scala_format_is_enabled':
            return is_enabled_in_view(view)
        return None
