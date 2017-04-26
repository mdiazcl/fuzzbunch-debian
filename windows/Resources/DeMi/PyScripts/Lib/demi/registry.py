# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: registry.py
import demi.windows
import dsz.env
import re
Kisu_IdRange = 3489660928
Longterm_IdRange = 2147483648

class ModuleId:

    def __init__(self, id, fileName, moduleName):
        Max = 268435456
        if id >= Max:
            raise StandardError('Base Id (0x%08x) cannot be equal to or greater than maximum (0x%08x)' % (id, Max))
        self.Id = id + Kisu_IdRange
        self.Name = fileName
        self.ModuleName = moduleName


PC = ModuleId(256, 'PC', 'PC')
DMGZ = ModuleId(257, 'ntfltmgr', 'DMGZ')
FLAV = ModuleId(258, 'ntevt', 'FLAV')