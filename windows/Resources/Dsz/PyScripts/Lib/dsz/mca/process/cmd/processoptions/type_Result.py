# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Result.py
from types import *

class Result:

    def __init__(self):
        self.__dict__['processId'] = 0
        self.__dict__['value'] = 0

    def __getattr__(self, name):
        if name == 'processId':
            return self.__dict__['processId']
        if name == 'value':
            return self.__dict__['value']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'processId':
            self.__dict__['processId'] = value
        elif name == 'value':
            self.__dict__['value'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_PROCESS_ID, self.__dict__['processId'])
        submsg.AddU32(MSG_KEY_RESULT_VALUE, self.__dict__['value'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['processId'] = submsg.FindU32(MSG_KEY_RESULT_PROCESS_ID)
        self.__dict__['value'] = submsg.FindU32(MSG_KEY_RESULT_VALUE)