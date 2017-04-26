# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Hide(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.HideObject = Hide.HideObject(dsz.cmd.data.Get('HideObject', dsz.TYPE_OBJECT)[0])
        except:
            self.HideObject = None

        try:
            self.UnhideObject = Hide.UnhideObject(dsz.cmd.data.Get('UnhideObject', dsz.TYPE_OBJECT)[0])
        except:
            self.UnhideObject = None

        return

    class HideObject(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
            except:
                self.value = None

            try:
                self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
            except:
                self.type = None

            try:
                self.data = dsz.cmd.data.ObjectGet(obj, 'data', dsz.TYPE_STRING)[0]
            except:
                self.data = None

            return

    class UnhideObject(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
            except:
                self.value = None

            try:
                self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
            except:
                self.type = None

            try:
                self.data = dsz.cmd.data.ObjectGet(obj, 'data', dsz.TYPE_STRING)[0]
            except:
                self.data = None

            return


dsz.data.RegisterCommand('Hide', Hide)
HIDE = Hide
hide = Hide