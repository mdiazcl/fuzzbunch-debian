# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py


def Lookup(Tech, Suffix):
    import dsz
    if Tech.upper() == '_PROV_MCL_MEMORY':
        Tech = '_PROV_MCL_NTMEMORY'
    envName = '%s_%s' % (Tech, Suffix)
    if dsz.env.Check(envName):
        providerStr = dsz.env.Get(envName)
        try:
            value = int(providerStr, 0)
            return (
             True, value)
        except:
            pass

    return (
     False, 0)