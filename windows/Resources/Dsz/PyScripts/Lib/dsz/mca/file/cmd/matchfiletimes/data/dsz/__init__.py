# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class MatchFileTimes(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.MatchFileTimesResults = MatchFileTimes.MatchFileTimesResults(dsz.cmd.data.Get('MatchFileTimesResults', dsz.TYPE_OBJECT)[0])
        except:
            self.MatchFileTimesResults = None

        return

    class MatchFileTimesResults(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.destfile = dsz.cmd.data.ObjectGet(obj, 'destfile', dsz.TYPE_STRING)[0]
            except:
                self.destfile = None

            try:
                self.sourcefile = dsz.cmd.data.ObjectGet(obj, 'sourcefile', dsz.TYPE_STRING)[0]
            except:
                self.sourcefile = None

            return


dsz.data.RegisterCommand('MatchFileTimes', MatchFileTimes)
MATCHFILETIMES = MatchFileTimes
matchfiletimes = MatchFileTimes