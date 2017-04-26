# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import _dsz
import dsz.control
import dsz.cmd
import dsz.env
import dsz.script
import dsz.ui
import sys
import time

def Sleep(ms, checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    _dsz.dszObj.sleep(ms)


def Timestamp():
    currentTime = time.time()
    gmt = time.gmtime(currentTime)
    fmt = '%Y_%m_%d_%Hh%Mm%Ss'
    return '%s.%03u' % (time.strftime(fmt, gmt), currentTime * 1000 % 1000)


DEFAULT = _dsz.dszObj.DEFAULT
GOOD = _dsz.dszObj.GOOD
WARNING = _dsz.dszObj.WARNING
ERROR = _dsz.dszObj.ERROR
RUN_FLAG_RECORD = _dsz.dszObj.RUN_FLAG_RECORD
RUN_FLAG_RECORD_NO_CLEAR = _dsz.dszObj.RUN_FLAG_RECORD_NO_CLEAR
TYPE_BOOL = _dsz.dszObj.TYPE_BOOL
TYPE_INT = _dsz.dszObj.TYPE_INT
TYPE_OBJECT = _dsz.dszObj.TYPE_OBJECT
TYPE_STRING = _dsz.dszObj.TYPE_STRING