# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Delete(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.deletionitem = list()
        try:
            for x in dsz.cmd.data.Get('deletionitem', dsz.TYPE_OBJECT):
                self.deletionitem.append(Delete.deletionitem(x))

        except:
            pass

    class deletionitem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.file = dsz.cmd.data.ObjectGet(obj, 'file', dsz.TYPE_STRING)[0]
            except:
                self.file = None

            try:
                self.delay = dsz.cmd.data.ObjectGet(obj, 'delay', dsz.TYPE_BOOL)[0]
            except:
                self.delay = None

            try:
                self.StatusValue = dsz.cmd.data.ObjectGet(obj, 'StatusValue', dsz.TYPE_INT)[0]
            except:
                self.StatusValue = None

            try:
                self.StatusString = dsz.cmd.data.ObjectGet(obj, 'StatusString', dsz.TYPE_STRING)[0]
            except:
                self.StatusString = None

            return


dsz.data.RegisterCommand('Delete', Delete)
DELETE = Delete
delete = Delete