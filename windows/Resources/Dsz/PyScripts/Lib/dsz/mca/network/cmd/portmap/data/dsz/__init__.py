# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Portmap(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.Process = list()
        try:
            for x in dsz.cmd.data.Get('Process', dsz.TYPE_OBJECT):
                self.Process.append(Portmap.Process(x))

        except:
            pass

    class Process(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.id = dsz.cmd.data.ObjectGet(obj, 'id', dsz.TYPE_INT)[0]
            except:
                self.id = None

            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            self.Port = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Port', dsz.TYPE_OBJECT):
                    self.Port.append(Portmap.Process.Port(x))

            except:
                pass

            return

        class Port(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.sourcePort = dsz.cmd.data.ObjectGet(obj, 'sourcePort', dsz.TYPE_INT)[0]
                except:
                    self.sourcePort = None

                try:
                    self.sourceAddr = dsz.cmd.data.ObjectGet(obj, 'sourceAddr', dsz.TYPE_STRING)[0]
                except:
                    self.sourceAddr = None

                try:
                    self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
                except:
                    self.type = None

                try:
                    self.state = dsz.cmd.data.ObjectGet(obj, 'state', dsz.TYPE_STRING)[0]
                except:
                    self.state = None

                return


dsz.data.RegisterCommand('Portmap', Portmap)
PORTMAP = Portmap
portmap = Portmap