# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\pyreadline\console\__init__.py
# Compiled at: 2011-10-07 02:48:04
import glob
import sys
success = False
in_ironpython = 'IronPython' in sys.version
if in_ironpython:
    try:
        from ironpython_console import *
        success = True
    except ImportError:
        raise

else:
    try:
        from console import *
        success = True
    except ImportError:
        raise

    if not success:
        raise ImportError('Could not find a console implementation for your platform')