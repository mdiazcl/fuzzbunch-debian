# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py


def CheckValue(name, globalValue=False):
    import dsz
    if globalValue:
        return dsz.env.Check(name, checkForStop=False)
    else:
        return dsz.env.Check(name, int(dsz.script.Env['script_command_id']), checkForStop=False)


def DeleteValue(name, globalValue=False):
    import dsz
    if globalValue:
        rtn = dsz.env.Delete(name, checkForStop=False)
    else:
        rtn = dsz.env.Delete(name, int(dsz.script.Env['script_command_id']), checkForStop=False)
    if not rtn:
        raise RuntimeError('Delete of %s env value failed' % name)


def GetValue(name, globalValue=False):
    import dsz
    if globalValue:
        return dsz.env.Get(name, checkForStop=False)
    else:
        return dsz.env.Get(name, int(dsz.script.Env['script_command_id']), checkForStop=False)


def SetValue(name, value, globalValue=False):
    import dsz
    if globalValue:
        rtn = dsz.env.Set(name, value, checkForStop=False)
    else:
        rtn = dsz.env.Set(name, value, int(dsz.script.Env['script_command_id']), checkForStop=False)
    if not rtn:
        raise RuntimeError('Set of %s env value failed' % name)