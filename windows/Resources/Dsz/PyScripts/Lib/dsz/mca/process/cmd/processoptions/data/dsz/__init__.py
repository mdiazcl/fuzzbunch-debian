# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class ProcessOptions(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.Options = list()
        try:
            for x in dsz.cmd.data.Get('Options', dsz.TYPE_OBJECT):
                self.Options.append(ProcessOptions.Options(x))

        except:
            pass

    class Options(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Permanent = dsz.cmd.data.ObjectGet(obj, 'Permanent', dsz.TYPE_BOOL)[0]
            except:
                self.Permanent = None

            try:
                self.ExecutionEnabled = dsz.cmd.data.ObjectGet(obj, 'ExecutionEnabled', dsz.TYPE_BOOL)[0]
            except:
                self.ExecutionEnabled = None

            try:
                self.ExecutionDisabled = dsz.cmd.data.ObjectGet(obj, 'ExecutionDisabled', dsz.TYPE_BOOL)[0]
            except:
                self.ExecutionDisabled = None

            try:
                self.ExecuteDispatchEnabled = dsz.cmd.data.ObjectGet(obj, 'ExecuteDispatchEnabled', dsz.TYPE_BOOL)[0]
            except:
                self.ExecuteDispatchEnabled = None

            try:
                self.DisableThunkEmulation = dsz.cmd.data.ObjectGet(obj, 'DisableThunkEmulation', dsz.TYPE_BOOL)[0]
            except:
                self.DisableThunkEmulation = None

            try:
                self.ImageDispatchEnabled = dsz.cmd.data.ObjectGet(obj, 'ImageDispatchEnabled', dsz.TYPE_BOOL)[0]
            except:
                self.ImageDispatchEnabled = None

            try:
                self.DisableExceptionChainValidation = dsz.cmd.data.ObjectGet(obj, 'DisableExceptionChainValidation', dsz.TYPE_BOOL)[0]
            except:
                self.DisableExceptionChainValidation = None

            try:
                self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_INT)[0]
            except:
                self.value = None

            try:
                self.processId = dsz.cmd.data.ObjectGet(obj, 'processId', dsz.TYPE_INT)[0]
            except:
                self.processId = None

            return


dsz.data.RegisterCommand('ProcessOptions', ProcessOptions)
PROCESSOPTIONS = ProcessOptions
processoptions = ProcessOptions