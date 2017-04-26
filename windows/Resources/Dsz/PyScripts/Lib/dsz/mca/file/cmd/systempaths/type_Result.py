# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Result.py
from types import *

class Result:

    def __init__(self):
        self.__dict__['windowsPath'] = ''
        self.__dict__['systemPath'] = ''
        self.__dict__['tempPath'] = ''

    def __getattr__(self, name):
        if name == 'windowsPath':
            return self.__dict__['windowsPath']
        if name == 'systemPath':
            return self.__dict__['systemPath']
        if name == 'tempPath':
            return self.__dict__['tempPath']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'windowsPath':
            self.__dict__['windowsPath'] = value
        elif name == 'systemPath':
            self.__dict__['systemPath'] = value
        elif name == 'tempPath':
            self.__dict__['tempPath'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_WINDOWS_PATH, self.__dict__['windowsPath'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_SYSTEM_PATH, self.__dict__['systemPath'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TEMP_PATH, self.__dict__['tempPath'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['windowsPath'] = submsg.FindString(MSG_KEY_RESULT_WINDOWS_PATH)
        self.__dict__['systemPath'] = submsg.FindString(MSG_KEY_RESULT_SYSTEM_PATH)
        self.__dict__['tempPath'] = submsg.FindString(MSG_KEY_RESULT_TEMP_PATH)