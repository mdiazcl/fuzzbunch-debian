# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class GeZu_KernelMemory(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.GeZu_KernelMemoryResponse = GeZu_KernelMemory.GeZu_KernelMemoryResponse(dsz.cmd.data.Get('GeZu_KernelMemoryResponse', dsz.TYPE_OBJECT)[0])
        except:
            self.GeZu_KernelMemoryResponse = None

        return

    class GeZu_KernelMemoryResponse(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.MemDump = dsz.cmd.data.ObjectGet(obj, 'MemDump', dsz.TYPE_STRING)[0]
            except:
                self.MemDump = None

            return


dsz.data.RegisterCommand('GeZu_KernelMemory', GeZu_KernelMemory)
GEZU_KERNELMEMORY = GeZu_KernelMemory
gezu_kernelmemory = GeZu_KernelMemory