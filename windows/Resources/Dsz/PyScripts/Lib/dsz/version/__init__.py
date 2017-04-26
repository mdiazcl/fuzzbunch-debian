# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.version.checks
import dsz.version.checks.windows
import dsz.version.checks.unix

def _getenvvalue(name, addr):
    if dsz.env.Check(name, 0, addr):
        return dsz.env.Get(name, 0, addr)
    else:
        return 'UNKNOWN'


def _getArch(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_ARCH', addr)


def _getCompiledArch(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_COMPILED_ARCH', addr)


def _getOs(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_OS', addr)


def _getCompiledOs(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_COMPILED_OS', addr)


def _getMajorVersion(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_MAJOR_VERSION', addr)


def _getMinorVersion(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_MINOR_VERSION', addr)


def _getOtherVersion(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_OTHER_VERSION', addr)


class Info:

    def __init__(self, addr=dsz.script.Env['target_address']):
        self.addr = addr
        self.arch = _getArch(addr)
        self.compiledArch = _getCompiledArch(addr)
        self.os = _getOs(addr)
        self.compiledOs = _getCompiledOs(addr)
        self.majorStr = _getMajorVersion(addr)
        self.minorStr = _getMinorVersion(addr)
        self.otherStr = _getOtherVersion(addr)
        try:
            self.major = int(self.majorStr)
        except:
            self.major = 0

        try:
            self.minor = int(self.minorStr)
        except:
            self.minor = 0

        try:
            self.other = int(self.otherStr)
        except:
            self.other = 0