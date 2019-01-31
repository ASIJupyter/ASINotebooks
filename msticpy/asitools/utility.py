# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""Miscellaneous helper methods for ASI Notebooks."""
import sys
from IPython.core.display import display, HTML

import pandas as pd


def string_empty(string):
    """Return True if the input string is None or whitespace."""
    return (string is None) or not (string and string.strip())


def is_not_empty(test_object):
    """Return True if the test_object is not None or empty."""
    if test_object:
        if isinstance(test_object, str):
            if test_object.strip():
                # test_object is not None AND myString is not empty or blank
                return True
            return False
        return True
    return False


# Toggle Code Cell Contents
_TOGGLE_CODE_STR = '''
<form action="javascript:code_toggle()">
    <input type="submit" id="toggleButton" value="Show/Hide Code">
</form>
'''

_TOGGLE_CODE_PREPARE_STR = '''
    <script>
    function code_toggle() {
        if ($('div.cell.code_cell.rendered.selected div.input').css('display')!='none'){
            $('div.cell.code_cell.rendered.selected div.input').hide();
        } else {
            $('div.cell.code_cell.rendered.selected div.input').show();
        }
    }
    </script>

'''


def toggle_code():
    """Display a toggle button to hide/reveal code cell."""
    display(HTML(_TOGGLE_CODE_STR))


# String escapes
def escape_windows_path(str_path):
    """Escape backslash characters in a string."""
    if is_not_empty(str_path):
        return str_path.replace('\\', '\\\\')
    return str_path


def unescape_windows_path(str_path):
    """Remove escaping from backslash characters in a string."""
    if is_not_empty(str_path):
        return str_path.replace('\\\\', '\\')
    return str_path


def export(func):
    """Decorate function or class to export to __all__."""
    mod = sys.modules[func.__module__]
    if hasattr(mod, '__all__'):
        mod.__all__.append(func.__name__)
    else:
        mod.__all__ = [func.__name__]
    return func


_PD_INSTALLED_VERSION = tuple(pd.__version__.split('.'))
_PD_VER_23 = ('0', '23', '0')


def pd_version_23() -> bool:
    """Return True if pandas version 0.23.0 or later is installed."""
    return _PD_INSTALLED_VERSION >= _PD_VER_23
