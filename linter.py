#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Yutin Liu (劉宇庭)
# Copyright (c) 2014 Yutin Liu (劉宇庭)
#
# License: MIT
#

"""This module exports the Lslint plugin class."""

from SublimeLinter.lint import PythonLinter, util


class Lslint(PythonLinter):

    """Provides an interface to lslint."""

    syntax = 'livescript'
    cmd = 'lslint --reporter xml'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.1.0'
    regex = (
        r'^\s+?<error line="(?P<line>\d+)" '
        r'column="(?P<col>\d+)" '
        # jscs always reports with error severity; show as warning
        r'severity="(?P<warning>error)" '
        r'message="(?P<message>.+?)"'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = 'ls'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
    module = 'lslint'
    check_version = False