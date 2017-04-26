# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\plugins\__init__.py
# Compiled at: 2013-02-27 18:39:54
import os
import glob
__all__ = []
for f in glob.glob(os.path.join(os.path.dirname(__file__), '*.py*')):
    __all__.append(os.path.split(os.path.splitext(f)[0])[1])