# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Wrappers(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.Wrappers = list()
        try:
            for x in dsz.cmd.data.Get('Wrappers', dsz.TYPE_OBJECT):
                self.Wrappers.append(Wrappers.Wrappers(x))

        except:
            pass

    class Wrappers(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.WrapperType = dsz.cmd.data.ObjectGet(obj, 'WrapperType', dsz.TYPE_STRING)[0]
            except:
                self.WrapperType = None

            self.Wrapper = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Wrapper', dsz.TYPE_OBJECT):
                    self.Wrapper.append(Wrappers.Wrappers.Wrapper(x))

            except:
                pass

            return

        class Wrapper(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Command = dsz.cmd.data.ObjectGet(obj, 'Command', dsz.TYPE_STRING)[0]
                except:
                    self.Command = None

                try:
                    self.Location = dsz.cmd.data.ObjectGet(obj, 'Location', dsz.TYPE_STRING)[0]
                except:
                    self.Location = None

                try:
                    self.Project = dsz.cmd.data.ObjectGet(obj, 'Project', dsz.TYPE_STRING)[0]
                except:
                    self.Project = None

                try:
                    self.Script = dsz.cmd.data.ObjectGet(obj, 'Script', dsz.TYPE_STRING)[0]
                except:
                    self.Script = None

                try:
                    self.ScriptArg = dsz.cmd.data.ObjectGet(obj, 'ScriptArg', dsz.TYPE_STRING)[0]
                except:
                    self.ScriptArg = None

                return


dsz.data.RegisterCommand('Wrappers', Wrappers)
WRAPPERS = Wrappers
wrappers = Wrappers