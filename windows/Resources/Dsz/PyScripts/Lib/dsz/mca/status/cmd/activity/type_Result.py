# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime

class Result:

    def __init__(self):
        self.__dict__['lastActivity'] = mcl.object.MclTime.MclTime()
        self.__dict__['moreData'] = False

    def __getattr__(self, name):
        if name == 'lastActivity':
            return self.__dict__['lastActivity']
        if name == 'moreData':
            return self.__dict__['moreData']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'lastActivity':
            self.__dict__['lastActivity'] = value
        elif name == 'moreData':
            self.__dict__['moreData'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddTime(MSG_KEY_RESULT_LAST_ACTIVITY, self.__dict__['lastActivity'])
        submsg.AddBool(MSG_KEY_RESULT_MORE_DATA, self.__dict__['moreData'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['lastActivity'] = submsg.FindTime(MSG_KEY_RESULT_LAST_ACTIVITY)
        self.__dict__['moreData'] = submsg.FindBool(MSG_KEY_RESULT_MORE_DATA)