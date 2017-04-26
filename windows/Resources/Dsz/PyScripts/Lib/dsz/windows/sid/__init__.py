# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz

def GetWellKnownSid(wellknown, addr=dsz.script.Env['target_address']):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    envName = '_WELLKNOWN_SID_%s' % wellknown
    if dsz.env.Check(envName, 0, addr):
        return dsz.env.Get(envName, 0, addr)
    if not dsz.cmd.Run('dst=%s sidlookup -wellknown "%s"' % (addr, wellknown), dsz.RUN_FLAG_RECORD):
        return wellknown
    try:
        name = dsz.cmd.data.Get('Sid::Name', dsz.TYPE_STRING)
        try:
            dsz.env.Set(envName, name[0], 0, addr)
        except:
            pass

        return name[0]
    except:
        return wellknown


def GetUserSid(sid, local=False, addr=dsz.script.Env['target_address']):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    envName = '_USER_SID_%s' % sid
    if dsz.env.Check(envName, 0, addr):
        return dsz.env.Get(envName, 0, addr)
    if not dsz.cmd.Run('dst=%s sidlookup -user -name "%s"' % (addr, sid), dsz.RUN_FLAG_RECORD):
        return sid
    try:
        name = dsz.cmd.data.Get('Sid::Name', dsz.TYPE_STRING)
        try:
            dsz.env.Set(envName, name[0], 0, addr)
        except:
            pass

        return name[0]
    except:
        return sid