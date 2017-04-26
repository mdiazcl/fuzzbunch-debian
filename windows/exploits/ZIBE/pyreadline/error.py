# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\pyreadline\error.py
# Compiled at: 2011-06-23 17:25:54


class ReadlineError(Exception):
    pass


class GetSetError(ReadlineError):
    pass