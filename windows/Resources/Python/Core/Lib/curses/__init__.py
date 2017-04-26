# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
"""curses

The main package for curses support for Python.  Normally used by importing
the package, and perhaps a particular module inside it.

   import curses
   from curses import textpad
   curses.initwin()
   ...

"""
__revision__ = '$Id$'
from _curses import *
from curses.wrapper import wrapper
import os as _os
import sys as _sys

def initscr():
    import _curses
    import curses
    setupterm(term=_os.environ.get('TERM', 'unknown'), fd=_sys.__stdout__.fileno())
    stdscr = _curses.initscr()
    for key, value in _curses.__dict__.items():
        if key[0:4] == 'ACS_' or key in ('LINES', 'COLS'):
            setattr(curses, key, value)

    return stdscr


def start_color():
    import _curses
    import curses
    retval = _curses.start_color()
    if hasattr(_curses, 'COLORS'):
        curses.COLORS = _curses.COLORS
    if hasattr(_curses, 'COLOR_PAIRS'):
        curses.COLOR_PAIRS = _curses.COLOR_PAIRS
    return retval


try:
    has_key
except NameError:
    from has_key import has_key