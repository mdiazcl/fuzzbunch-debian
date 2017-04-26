# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class LpDirectory(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.DirectoryItem = LpDirectory.DirectoryItem(dsz.cmd.data.Get('DirectoryItem', dsz.TYPE_OBJECT)[0])
        except:
            self.DirectoryItem = None

        return

    class DirectoryItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.dir = dsz.cmd.data.ObjectGet(obj, 'dir', dsz.TYPE_STRING)[0]
            except:
                self.dir = None

            return


dsz.data.RegisterCommand('LpDirectory', LpDirectory)
LPDIRECTORY = LpDirectory
lpdirectory = LpDirectory