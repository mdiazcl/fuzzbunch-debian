# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: settings.py.override
import dsz

def CheckConfigLocal():
    if dsz.ui.Prompt('Do you want to configure with FC?', True):
        return False
    else:
        return True


def Finalize(payloadFile):
    return dsz.cmd.Run('python Payload/_Prep.py -args "-action disable -file %s"' % payloadFile)