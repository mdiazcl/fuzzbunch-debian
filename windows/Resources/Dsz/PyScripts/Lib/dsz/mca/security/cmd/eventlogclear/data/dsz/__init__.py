# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class EventLogClear(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.taskinginfo = EventLogClear.taskinginfo(dsz.cmd.data.Get('taskinginfo', dsz.TYPE_OBJECT)[0])
        except:
            self.taskinginfo = None

        return

    class taskinginfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.recursive = dsz.cmd.data.ObjectGet(obj, 'recursive', dsz.TYPE_BOOL)[0]
            except:
                self.recursive = None

            try:
                self.searchpath = EventLogClear.taskinginfo.searchpath(dsz.cmd.data.ObjectGet(obj, 'searchpath', dsz.TYPE_OBJECT)[0])
            except:
                self.searchpath = None

            try:
                self.target = EventLogClear.taskinginfo.target(dsz.cmd.data.ObjectGet(obj, 'target', dsz.TYPE_OBJECT)[0])
            except:
                self.target = None

            return

        class searchpath(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return

        class target(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.location = dsz.cmd.data.ObjectGet(obj, 'location', dsz.TYPE_STRING)[0]
                except:
                    self.location = None

                try:
                    self.local = dsz.cmd.data.ObjectGet(obj, 'local', dsz.TYPE_BOOL)[0]
                except:
                    self.local = None

                return


dsz.data.RegisterCommand('EventLogClear', EventLogClear)
EVENTLOGCLEAR = EventLogClear
eventlogclear = EventLogClear