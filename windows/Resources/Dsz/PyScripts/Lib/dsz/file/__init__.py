# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz

def Exists(file, path=''):
    if len(path) == 0:
        cmd = 'dir "%s"' % file
    else:
        cmd = 'dir -path "%s/" -mask "%s"' % (path, file)
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not dsz.cmd.Run(cmd, dsz.RUN_FLAG_RECORD):
        raise RuntimeError, 'Dir command failed'
    try:
        return dsz.cmd.data.Size('DirItem::FileItem') > 0
    except:
        return False


def GetNames(file, path=''):
    if len(path) == 0:
        cmd = 'dir "%s"' % file
    else:
        cmd = 'dir -path "%s/" -mask "%s"' % (path, file)
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not dsz.cmd.Run(cmd, dsz.RUN_FLAG_RECORD):
        raise RuntimeError, 'Dir command failed'
    try:
        return dsz.cmd.data.Get('DirItem::FileItem::name', dsz.TYPE_STRING)
    except:
        return list()