# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Put(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.LocalFile = Put.LocalFile(dsz.cmd.data.Get('LocalFile', dsz.TYPE_OBJECT)[0])
        except:
            self.LocalFile = None

        try:
            self.File = Put.File(dsz.cmd.data.Get('File', dsz.TYPE_OBJECT)[0])
        except:
            self.File = None

        return

    class LocalFile(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.size = dsz.cmd.data.ObjectGet(obj, 'size', dsz.TYPE_INT)[0]
            except:
                self.size = None

            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            return

    class File(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            return


dsz.data.RegisterCommand('Put', Put)
PUT = Put
put = Put