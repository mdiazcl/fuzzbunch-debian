# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Move(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.MoveResults = Move.MoveResults(dsz.cmd.data.Get('MoveResults', dsz.TYPE_OBJECT)[0])
        except:
            self.MoveResults = None

        return

    class MoveResults(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.delay = dsz.cmd.data.ObjectGet(obj, 'delay', dsz.TYPE_BOOL)[0]
            except:
                self.delay = None

            try:
                self.destination = dsz.cmd.data.ObjectGet(obj, 'destination', dsz.TYPE_STRING)[0]
            except:
                self.destination = None

            try:
                self.source = dsz.cmd.data.ObjectGet(obj, 'source', dsz.TYPE_STRING)[0]
            except:
                self.source = None

            return


dsz.data.RegisterCommand('Move', Move)
MOVE = Move
move = Move