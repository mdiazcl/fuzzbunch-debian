# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class DllLoad(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.DllLoad = DllLoad.DllLoad(dsz.cmd.data.Get('DllLoad', dsz.TYPE_OBJECT)[0])
        except:
            self.DllLoad = None

        try:
            self.DllUnload = DllLoad.DllUnload(dsz.cmd.data.Get('DllUnload', dsz.TYPE_OBJECT)[0])
        except:
            self.DllUnload = None

        return

    class DllLoad(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.LoadAddress = dsz.cmd.data.ObjectGet(obj, 'LoadAddress', dsz.TYPE_INT)[0]
            except:
                self.LoadAddress = None

            return

    class DllUnload(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Unloaded = dsz.cmd.data.ObjectGet(obj, 'Unloaded', dsz.TYPE_BOOL)[0]
            except:
                self.Unloaded = None

            return


dsz.data.RegisterCommand('DllLoad', DllLoad)
DLLLOAD = DllLoad
dllload = DllLoad