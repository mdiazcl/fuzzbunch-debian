# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py


def ImportNamesWithNamespace(namespace, module, callerGlobals):
    _temp = __import__(namespace + module, callerGlobals, locals(), [module], -1)
    reload(_temp)
    for name in _temp.__dict__.keys():
        if not name.startswith('_'):
            callerGlobals[name] = _temp.__dict__[name]


def ImportWithNamespace(namespace, module, callerGlobals=None):
    _temp = __import__(namespace + module, callerGlobals, locals(), [module], -1)
    reload(_temp)
    if len(namespace) > 0 and callerGlobals != None:
        import sys
        topName = module.partition('.')[0]
        callerGlobals[topName] = sys.modules[namespace + topName]
    return