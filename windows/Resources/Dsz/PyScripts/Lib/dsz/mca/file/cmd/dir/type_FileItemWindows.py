# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_FileItemWindows.py
from types import *

class FileItemWindows:

    def __init__(self):
        self.__dict__['shortName'] = ''

    def __getattr__(self, name):
        if name == 'shortName':
            return self.__dict__['shortName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'shortName':
            self.__dict__['shortName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_FILE_ITEM_WINDOWS_SHORT_NAME, self.__dict__['shortName'])
        mmsg.AddMessage(MSG_KEY_FILE_ITEM_WINDOWS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_FILE_ITEM_WINDOWS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['shortName'] = submsg.FindString(MSG_KEY_FILE_ITEM_WINDOWS_SHORT_NAME)