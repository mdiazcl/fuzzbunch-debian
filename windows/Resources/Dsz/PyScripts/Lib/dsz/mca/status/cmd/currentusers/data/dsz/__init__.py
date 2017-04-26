# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class CurrentUsers(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.User = CurrentUsers.User(dsz.cmd.data.Get('User', dsz.TYPE_OBJECT)[0])
        except:
            self.User = None

        return

    class User(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.SessionId = dsz.cmd.data.ObjectGet(obj, 'SessionId', dsz.TYPE_INT)[0]
            except:
                self.SessionId = None

            try:
                self.LoginPid = dsz.cmd.data.ObjectGet(obj, 'LoginPid', dsz.TYPE_INT)[0]
            except:
                self.LoginPid = None

            try:
                self.Host = dsz.cmd.data.ObjectGet(obj, 'Host', dsz.TYPE_STRING)[0]
            except:
                self.Host = None

            try:
                self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
            except:
                self.Name = None

            try:
                self.Device = dsz.cmd.data.ObjectGet(obj, 'Device', dsz.TYPE_STRING)[0]
            except:
                self.Device = None

            return


dsz.data.RegisterCommand('CurrentUsers', CurrentUsers)
CURRENTUSERS = CurrentUsers
currentusers = CurrentUsers