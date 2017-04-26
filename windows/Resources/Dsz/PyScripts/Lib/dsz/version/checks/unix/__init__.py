# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz

def IsLinux(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'linux' or ver.os == 'linux_se':
        return True
    else:
        return False


def IsSeLinux(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'linux_se':
        return True
    else:
        return False


def IsSolaris(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'solaris':
        return True
    else:
        return False