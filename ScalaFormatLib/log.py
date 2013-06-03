"""
Copyright (c) 2012 Timon Wong

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import print_function

import sys
import traceback


NAME = 'ScalaFormat:'


def write_log(level, fmtstr, *args):
    print(NAME, '[' + level + ']', fmtstr % args)


def info(fmtstr, *args):
    write_log('INFO', fmtstr, *args)


def warning(fmtstr, *args):
    write_log('WARNING', fmtstr, *args)


def error(fmtstr, *args):
    write_log('ERROR', fmtstr, *args)


def exception(fmtstr, *args):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exception_message = traceback.format_exception(
        exc_type, exc_value, exc_traceback
    )
    write_log('ERROR', fmtstr, *args)
    print(''.join(['  ' + line for line in exception_message]))
