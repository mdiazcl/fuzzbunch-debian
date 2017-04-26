# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: TaskId.py


class TaskId:

    def GenerateAsString():
        import uuid
        from md5 import md5
        simpleUuid = uuid.uuid1()
        finalUuid = uuid.UUID(md5(simpleUuid.bytes).hexdigest())
        return str(finalUuid)

    def StrToIntArray(origStr):
        import math
        v = filter(lambda c: c not in '-', origStr)
        l = 2
        listTaskId = [ v[i * l:(i + 1) * l] for i in range(int(math.ceil(len(v) / float(l)))) ]
        arrayTaskId = [ int(s, 16) for s in listTaskId ]
        return arrayTaskId

    GenerateAsString = staticmethod(GenerateAsString)
    StrToIntArray = staticmethod(StrToIntArray)