# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import string

def _getenvvalue(name, addr):
    if dsz.env.Check(name, 0, addr):
        return dsz.env.Get(name, 0, addr)
    else:
        return 'UNKNOWN'


def IsOs64Bit(addr=dsz.script.Env['target_address']):
    answer = string.lower(_getenvvalue('_OS_64BIT', addr))
    if answer == 'yes' or answer == 'true':
        return True
    else:
        return False


def IsUnix(addr=dsz.script.Env['target_address']):
    return not dsz.version.checks.IsWindows(addr)


def IsWindows(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' or ver.os == 'win9x':
        return True
    else:
        return False