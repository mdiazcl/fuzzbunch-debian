# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Result.py
from types import *
import array
import array
RESULT_PERSISTENCE_TYPE_SOTI = 1
RESULT_PERSISTENCE_TYPE_LAUNCHER = 2
RESULT_PERSISTENCE_TYPE_JUVI = 3
RESULT_CRYPTO_KEY_LENGTH = 3

class ResultInstance:

    def __init__(self):
        self.__dict__['id'] = 0
        self.__dict__['versionMajor'] = 0
        self.__dict__['versionMinor'] = 0
        self.__dict__['versionFix'] = 0
        self.__dict__['versionBuild'] = 0

    def __getattr__(self, name):
        if name == 'id':
            return self.__dict__['id']
        if name == 'versionMajor':
            return self.__dict__['versionMajor']
        if name == 'versionMinor':
            return self.__dict__['versionMinor']
        if name == 'versionFix':
            return self.__dict__['versionFix']
        if name == 'versionBuild':
            return self.__dict__['versionBuild']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'id':
            self.__dict__['id'] = value
        elif name == 'versionMajor':
            self.__dict__['versionMajor'] = value
        elif name == 'versionMinor':
            self.__dict__['versionMinor'] = value
        elif name == 'versionFix':
            self.__dict__['versionFix'] = value
        elif name == 'versionBuild':
            self.__dict__['versionBuild'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_INSTANCE_ID, self.__dict__['id'])
        submsg.AddU32(MSG_KEY_RESULT_INSTANCE_VERSION_MAJOR, self.__dict__['versionMajor'])
        submsg.AddU32(MSG_KEY_RESULT_INSTANCE_VERSION_MINOR, self.__dict__['versionMinor'])
        submsg.AddU32(MSG_KEY_RESULT_INSTANCE_VERSION_FIX, self.__dict__['versionFix'])
        submsg.AddU32(MSG_KEY_RESULT_INSTANCE_VERSION_BUILD, self.__dict__['versionBuild'])
        mmsg.AddMessage(MSG_KEY_RESULT_INSTANCE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_INSTANCE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_INSTANCE_ID)
        self.__dict__['versionMajor'] = submsg.FindU32(MSG_KEY_RESULT_INSTANCE_VERSION_MAJOR)
        self.__dict__['versionMinor'] = submsg.FindU32(MSG_KEY_RESULT_INSTANCE_VERSION_MINOR)
        self.__dict__['versionFix'] = submsg.FindU32(MSG_KEY_RESULT_INSTANCE_VERSION_FIX)
        self.__dict__['versionBuild'] = submsg.FindU32(MSG_KEY_RESULT_INSTANCE_VERSION_BUILD)


class ResultConfigKey:

    def __init__(self):
        self.__dict__['path'] = ''
        self.__dict__['value'] = ''

    def __getattr__(self, name):
        if name == 'path':
            return self.__dict__['path']
        if name == 'value':
            return self.__dict__['value']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'path':
            self.__dict__['path'] = value
        elif name == 'value':
            self.__dict__['value'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_CONFIG_KEY_PATH, self.__dict__['path'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_CONFIG_KEY_VALUE, self.__dict__['value'])
        mmsg.AddMessage(MSG_KEY_RESULT_CONFIG_KEY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_CONFIG_KEY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['path'] = submsg.FindString(MSG_KEY_RESULT_CONFIG_KEY_PATH)
        self.__dict__['value'] = submsg.FindString(MSG_KEY_RESULT_CONFIG_KEY_VALUE)


class ResultConfigBase:

    def __init__(self):
        self.__dict__['instance'] = ResultInstance()
        self.__dict__['persistenceMethod'] = 0
        self.__dict__['cryptoKey'] = array.array('L')
        i = 0
        while i < RESULT_CRYPTO_KEY_LENGTH:
            self.__dict__['cryptoKey'].append(0)
            i = i + 1

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'persistenceMethod':
            return self.__dict__['persistenceMethod']
        if name == 'cryptoKey':
            return self.__dict__['cryptoKey']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'persistenceMethod':
            self.__dict__['persistenceMethod'] = value
        elif name == 'cryptoKey':
            self.__dict__['cryptoKey'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg2 = MarshalMessage()
        self.__dict__['instance'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_RESULT_CONFIG_BASE_CONFIG_INSTANCE, submsg2)
        submsg.AddU8(MSG_KEY_RESULT_CONFIG_BASE_PERSISTENCE_METHOD, self.__dict__['persistenceMethod'])
        submsg.AddData(MSG_KEY_RESULT_CONFIG_BASE_CRYPTO_KEY, self.__dict__['cryptoKey'])
        mmsg.AddMessage(MSG_KEY_RESULT_CONFIG_BASE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_CONFIG_BASE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        submsg2 = submsg.FindMessage(MSG_KEY_RESULT_CONFIG_BASE_CONFIG_INSTANCE)
        self.__dict__['instance'].Demarshal(submsg2)
        self.__dict__['persistenceMethod'] = submsg.FindU8(MSG_KEY_RESULT_CONFIG_BASE_PERSISTENCE_METHOD)
        self.__dict__['cryptoKey'] = submsg.FindData(MSG_KEY_RESULT_CONFIG_BASE_CRYPTO_KEY)


class ResultModule:

    def __init__(self):
        self.__dict__['size'] = 0
        self.__dict__['order'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['id'] = 0
        self.__dict__['moduleName'] = ''
        self.__dict__['processName'] = ''
        self.__dict__['hash'] = array.array('B')

    def __getattr__(self, name):
        if name == 'size':
            return self.__dict__['size']
        if name == 'order':
            return self.__dict__['order']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'id':
            return self.__dict__['id']
        if name == 'moduleName':
            return self.__dict__['moduleName']
        if name == 'processName':
            return self.__dict__['processName']
        if name == 'hash':
            return self.__dict__['hash']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'size':
            self.__dict__['size'] = value
        elif name == 'order':
            self.__dict__['order'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'id':
            self.__dict__['id'] = value
        elif name == 'moduleName':
            self.__dict__['moduleName'] = value
        elif name == 'processName':
            self.__dict__['processName'] = value
        elif name == 'hash':
            self.__dict__['hash'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_MODULE_SIZE, self.__dict__['size'])
        submsg.AddU32(MSG_KEY_RESULT_MODULE_ORDER, self.__dict__['order'])
        submsg.AddU32(MSG_KEY_RESULT_MODULE_FLAGS, self.__dict__['flags'])
        submsg.AddU32(MSG_KEY_RESULT_MODULE_ID, self.__dict__['id'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_MODULE_MODULE_NAME, self.__dict__['moduleName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_MODULE_PROCESS_NAME, self.__dict__['processName'])
        submsg.AddData(MSG_KEY_RESULT_MODULE_HASH, self.__dict__['hash'])
        mmsg.AddMessage(MSG_KEY_RESULT_MODULE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MODULE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['size'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_SIZE)
        self.__dict__['order'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_ORDER)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_FLAGS)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_ID)
        self.__dict__['moduleName'] = submsg.FindString(MSG_KEY_RESULT_MODULE_MODULE_NAME)
        self.__dict__['processName'] = submsg.FindString(MSG_KEY_RESULT_MODULE_PROCESS_NAME)
        try:
            self.__dict__['hash'] = submsg.FindData(MSG_KEY_RESULT_MODULE_HASH)
        except:
            pass


class ResultModuleLoad:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['id'] = 0
        self.__dict__['moduleHandle'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'id':
            return self.__dict__['id']
        if name == 'moduleHandle':
            return self.__dict__['moduleHandle']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'id':
            self.__dict__['id'] = value
        elif name == 'moduleHandle':
            self.__dict__['moduleHandle'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_MODULE_LOAD_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_RESULT_MODULE_LOAD_ID, self.__dict__['id'])
        submsg.AddU64(MSG_KEY_RESULT_MODULE_LOAD_MODULE_HANDLE, self.__dict__['moduleHandle'])
        mmsg.AddMessage(MSG_KEY_RESULT_MODULE_LOAD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MODULE_LOAD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_LOAD_INSTANCE)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_LOAD_ID)
        self.__dict__['moduleHandle'] = submsg.FindU64(MSG_KEY_RESULT_MODULE_LOAD_MODULE_HANDLE)


class ResultModuleRead:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['id'] = 0
        self.__dict__['data'] = array.array('B')

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'id':
            return self.__dict__['id']
        if name == 'data':
            return self.__dict__['data']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'id':
            self.__dict__['id'] = value
        elif name == 'data':
            self.__dict__['data'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_MODULE_READ_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_RESULT_MODULE_READ_ID, self.__dict__['id'])
        submsg.AddData(MSG_KEY_RESULT_MODULE_READ_DATA, self.__dict__['data'])
        mmsg.AddMessage(MSG_KEY_RESULT_MODULE_READ, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MODULE_READ, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_READ_INSTANCE)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_READ_ID)
        self.__dict__['data'] = submsg.FindData(MSG_KEY_RESULT_MODULE_READ_DATA)


class ResultModuleAdd:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['id'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'id':
            return self.__dict__['id']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'id':
            self.__dict__['id'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_MODULE_ADD_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_RESULT_MODULE_ADD_ID, self.__dict__['id'])
        mmsg.AddMessage(MSG_KEY_RESULT_MODULE_ADD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MODULE_ADD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_ADD_INSTANCE)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_ADD_ID)


class ResultModuleDelete:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['id'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'id':
            return self.__dict__['id']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'id':
            self.__dict__['id'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_MODULE_DELETE_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_RESULT_MODULE_DELETE_ID, self.__dict__['id'])
        mmsg.AddMessage(MSG_KEY_RESULT_MODULE_DELETE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MODULE_DELETE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_DELETE_INSTANCE)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_DELETE_ID)


class ResultModuleFree:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['moduleHandle'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'moduleHandle':
            return self.__dict__['moduleHandle']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'moduleHandle':
            self.__dict__['moduleHandle'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_MODULE_FREE_INSTANCE, self.__dict__['instance'])
        submsg.AddU64(MSG_KEY_RESULT_MODULE_FREE_HANDLE, self.__dict__['moduleHandle'])
        mmsg.AddMessage(MSG_KEY_RESULT_MODULE_FREE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MODULE_FREE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_FREE_INSTANCE)
        self.__dict__['moduleHandle'] = submsg.FindU64(MSG_KEY_RESULT_MODULE_FREE_HANDLE)


class ResultDriverLoad:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['id'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'id':
            return self.__dict__['id']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'id':
            self.__dict__['id'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_DRIVER_LOAD_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_RESULT_DRIVER_LOAD_ID, self.__dict__['id'])
        mmsg.AddMessage(MSG_KEY_RESULT_DRIVER_LOAD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_DRIVER_LOAD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_RESULT_DRIVER_LOAD_INSTANCE)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_DRIVER_LOAD_ID)


class ResultDriverUnload:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['id'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'id':
            return self.__dict__['id']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'id':
            self.__dict__['id'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_DRIVER_UNLOAD_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_RESULT_DRIVER_UNLOAD_ID, self.__dict__['id'])
        mmsg.AddMessage(MSG_KEY_RESULT_DRIVER_UNLOAD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_DRIVER_UNLOAD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_RESULT_DRIVER_UNLOAD_INSTANCE)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_DRIVER_UNLOAD_ID)


class ResultProcessLoad:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['processId'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'processId':
            return self.__dict__['processId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'processId':
            self.__dict__['processId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_PROCESS_LOAD_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_RESULT_PROCESS_LOAD_PROCESS_ID, self.__dict__['processId'])
        mmsg.AddMessage(MSG_KEY_RESULT_PROCESS_LOAD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_PROCESS_LOAD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_RESULT_PROCESS_LOAD_INSTANCE)
        self.__dict__['processId'] = submsg.FindU32(MSG_KEY_RESULT_PROCESS_LOAD_PROCESS_ID)


class ResultConnect:

    def __init__(self):
        self.__dict__['instance'] = ResultInstance()

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg2 = MarshalMessage()
        self.__dict__['instance'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_RESULT_CONNECT_INSTANCE, submsg2)
        mmsg.AddMessage(MSG_KEY_RESULT_CONNECT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_CONNECT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        submsg2 = submsg.FindMessage(MSG_KEY_RESULT_CONNECT_INSTANCE)
        self.__dict__['instance'].Demarshal(submsg2)