# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Result.py
from types import *
import mcl.object.IpAddr

class Result:

    def __init__(self):
        self.__dict__['addr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'addr':
            return self.__dict__['addr']
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'addr':
            self.__dict__['addr'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddIpAddr(MSG_KEY_RESULT_ADDRESS, self.__dict__['addr'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['addr'] = submsg.FindIpAddr(MSG_KEY_RESULT_ADDRESS)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_NAME)