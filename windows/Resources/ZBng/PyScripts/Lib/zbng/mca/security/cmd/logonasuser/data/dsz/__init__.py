# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class LogonAsUser(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.logon = LogonAsUser.logon(dsz.cmd.data.Get('logon', dsz.TYPE_OBJECT)[0])
        except:
            self.logon = None

        return

    class logon(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.handle = dsz.cmd.data.ObjectGet(obj, 'handle', dsz.TYPE_INT)[0]
            except:
                self.handle = None

            try:
                self.alias = dsz.cmd.data.ObjectGet(obj, 'alias', dsz.TYPE_STRING)[0]
            except:
                self.alias = None

            return


dsz.data.RegisterCommand('LogonAsUser', LogonAsUser)
LOGONASUSER = LogonAsUser
logonasuser = LogonAsUser