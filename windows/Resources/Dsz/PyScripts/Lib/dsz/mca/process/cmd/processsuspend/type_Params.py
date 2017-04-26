# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Params.py
from types import *
PARAMS_TYPE_SUSPEND = 1

class Params:

    def __init__(self):
        self.__dict__['pid'] = 0
        self.__dict__['force'] = False
        self.__dict__['suspend'] = False

    def __getattr__(self, name):
        if name == 'pid':
            return self.__dict__['pid']
        if name == 'force':
            return self.__dict__['force']
        if name == 'suspend':
            return self.__dict__['suspend']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'pid':
            self.__dict__['pid'] = value
        elif name == 'force':
            self.__dict__['force'] = value
        elif name == 'suspend':
            self.__dict__['suspend'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_PROCESS_ID, self.__dict__['pid'])
        submsg.AddBool(MSG_KEY_PARAMS_FORCE, self.__dict__['force'])
        submsg.AddBool(MSG_KEY_PARAMS_SUSPEND, self.__dict__['suspend'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['pid'] = submsg.FindU32(MSG_KEY_PARAMS_PROCESS_ID)
        self.__dict__['force'] = submsg.FindBool(MSG_KEY_PARAMS_FORCE)
        self.__dict__['suspend'] = submsg.FindBool(MSG_KEY_PARAMS_SUSPEND)