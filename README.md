ScalaFormat
============

Summary
-------

ScalaFormat is a scala code formatter plugin for [Sublime Text]. It is rewritten
from [Takafumi Ikeda]'s [Sublime Scalariform] plugin, with following enhancements:

* Formatting buffer instead of formatting source file directly.
* Auto format on file save support (disabled by default).
* Sublime Text 3 support.

[Sublime Text]: http://www.sublimetext.com/
[Takafumi Ikeda]: https://github.com/ikeike443
[Sublime Scalariform]: https://github.com/ikeike443/Sublime-Scalariform


Prerequisites
-------------

* Java™ 5 or later.
* Patience :) - It may take a few seconds before scalariform finished.


Installation
------------

### With the Package Control plugin

The easiest way to install ScalaFormat is through [Package Control].

[Package Control]: http://wbond.net/sublime_packages/package_control

Once you have Package Control installed, restart Sublime Text.

1. Bring up the Command Palette (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>
   under Windows and Linux; <kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>P</kbd> under OS X).
2. Type "Install" and select "Package Control: Install Package".
3. Select "ScalaFormat" from list.

The advantage of using Package Control is that it will keep ScalaFormat up to
date automatically.

### Manual Install

**Without Git:**
[Download](https://github.com/timonwong/ScalaFormat) the latest source code, and
extract to the Packages directory.

**With Git:**
Type the following command in your Sublime Text 2 Packages directory:

`git clone git://github.com/timonwong/ScalaFormat.git`

The "Packages" directory is located at:

* **Windows:**  `%APPDATA%\Sublime Text 2\Packages\`
* **Linux:**    `~/.config/sublime-text-2/Packages/`
* **OS X:**     `~/Library/Application Support/Sublime Text 2/Packages/`

Usage
-----

### Key Bindings

The default key bindings for this plugin:

* <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>F</kbd>: Format current file.

### Command Palette

Open the command palette, it apperas as `ScalaFormat: Format Current File`.

Settings
--------

```javascript
{
    // If the executable is not in the system path, you may have to set the java executable manually
    "java_executable": "java",
    // Auto format on file save
    "autoformat_on_save": false,
    // scalariform command line options - preferences
    // https://github.com/mdr/scalariform/wiki/Command-line-tool
    "scalariform": {
        // Enable/disable Align parameters on different lines in the same column
        "alignParameters": false,
        // Enable/disable Align the arrows of consecutive single-line case statements
        "alignSingleLineCaseStatements": false,
        // Set Maximum number of spaces inserted before an arrow to align case statements: [1-100]
        "alignSingleLineCaseStatements.maxArrowIndent": 40,
        // Enable/disable Compact Control Readability style
        "compactControlReadability": false,
        // Enable/disable Omit spaces when formatting a '+' operator on String literals
        "compactStringConcatenation": false,
        // Enable/disable Double indent either a class's parameters or its inheritance list
        "doubleIndentClassDeclaration": false,
        // Enable/disable Format XML literals
        "formatXml": true,
        // Enable/disable Indent local defs an extra level
        "indentLocalDefs": false,
        // Enable/disable Indent package blocks
        "indentPackageBlocks": true,
        // Set Number of spaces to use for indentation: [1-10]
        "indentSpaces": 2,
        // Enable/disable Use a tab character for indentation
        "indentWithTabs": false,
        // Enable/disable Start multiline Scaladoc comment body on same line as the opening '/**'
        "multilineScaladocCommentsStartOnFirstLine": false,
        // Enable/disable Allow a newline before a ')' in an argument expression
        "preserveDanglingCloseParenthesis": false,
        // Enable/disable Place Scaladoc asterisks beneath the second asterisk in the opening '/**', as opposed to the first
        "placeScaladocAsterisksBeneathSecondAsterisk": false,
        // Enable/disable Preserve a space before a parenthesis argument
        "preserveSpaceBeforeArguments": false,
        // Enable/disable Replace arrow tokens with unicode, equivalents: => with ⇒, and <- with ←
        "rewriteArrowSymbols": false,
        // Enable/disable Add a space before colons
        "spaceBeforeColon": false,
        // Enable/disable Require a space after '[' and before ']'
        "spaceInsideBrackets": false,
        // Enable/disable Require a space after '(' and before ')'
        "spaceInsideParentheses": false,
        // Enable/disable Add a space around the @ token in pattern binders
        "spacesWithinPatternBinders": true
    }
}
```

What's New
==========

v1.1.1 (July 15, 2013)

* Fix compatibility with Sublime Text 3 and Packge Control.

v1.1 (June 3, 2013)

* Add support for Sublime Text 3.
* Updated scalariform excutable.

v1.0

* First release.

License
-------

This plugin released under MIT License:

    Copyright (c) 2012-2013 Timon Wong
    Portions Copyright (c) 2012 Takafumi Ikeda

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
