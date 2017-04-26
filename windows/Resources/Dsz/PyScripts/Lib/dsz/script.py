# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: script.py
import _dsz
import sys
Env = _dsz.dszObj.env

def CheckStop(shouldExit=True):
    if _dsz.dszObj.check_for_stop():
        if shouldExit:
            sys.exit(-1)
        else:
            return True
    return False


def IsLocal():
    if _dsz.dszObj.env['script_running_locally'] == 'true':
        return True
    else:
        return False


class data:

    def Add(name, value, type, checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.script_data_add(name, value, type)

    def Clear(checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.script_data_clear()

    def End(checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.script_data_end()

    def Start(name, checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.script_data_start(name)

    def Store(checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.script_data_store()

    Add = staticmethod(Add)
    Clear = staticmethod(Clear)
    End = staticmethod(End)
    Start = staticmethod(Start)
    Store = staticmethod(Store)