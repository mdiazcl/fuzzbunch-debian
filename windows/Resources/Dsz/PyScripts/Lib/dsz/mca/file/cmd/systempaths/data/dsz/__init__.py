# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class SystemPaths(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.WindowsDir = SystemPaths.WindowsDir(dsz.cmd.data.Get('WindowsDir', dsz.TYPE_OBJECT)[0])
        except:
            self.WindowsDir = None

        try:
            self.SystemDir = SystemPaths.SystemDir(dsz.cmd.data.Get('SystemDir', dsz.TYPE_OBJECT)[0])
        except:
            self.SystemDir = None

        try:
            self.TempDir = SystemPaths.TempDir(dsz.cmd.data.Get('TempDir', dsz.TYPE_OBJECT)[0])
        except:
            self.TempDir = None

        return

    class WindowsDir(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.location = dsz.cmd.data.ObjectGet(obj, 'location', dsz.TYPE_STRING)[0]
            except:
                self.location = None

            return

    class SystemDir(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.location = dsz.cmd.data.ObjectGet(obj, 'location', dsz.TYPE_STRING)[0]
            except:
                self.location = None

            return

    class TempDir(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.location = dsz.cmd.data.ObjectGet(obj, 'location', dsz.TYPE_STRING)[0]
            except:
                self.location = None

            return


dsz.data.RegisterCommand('SystemPaths', SystemPaths)
SYSTEMPATHS = SystemPaths
systempaths = SystemPaths