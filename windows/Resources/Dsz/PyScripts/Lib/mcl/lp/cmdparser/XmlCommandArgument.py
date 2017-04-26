# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: XmlCommandArgument.py
from XmlCommandBase import XmlCommandBase

class XmlCommandArgument(XmlCommandBase):

    def __init__(self):
        XmlCommandBase.__init__(self)
        self.m_group = ''
        self.m_validValues = {}

    def AddValidValueData(self, value, dataName, dataValue):
        if len(value) == 0 or len(dataName) == 0:
            raise RuntimeError('Invalid value/dataName')
        if not self.m_validValues.has_key(value):
            dataMap = {dataName: dataValue}
            paramMap = {}
            self.m_validValues[value] = (paramMap, dataMap)
        else:
            if self.m_validValues[value][1].has_key(dataName):
                raise RuntimeError("Duplicate data name (%s) found for value '%s'" % (dataName, value))
            self.m_validValues[value][1][dataName] = dataValue

    def AddValidValueParam(self, value, paramName, paramValue):
        if len(value) == 0 or len(paramValue) == 0:
            raise RuntimeError('Invalid value/paramValue')
        if not self.m_validValues.has_key(value):
            dataMap = {}
            paramMap = {paramName: paramValue}
            self.m_validValues[value] = (paramMap, dataMap)
        else:
            if self.m_validValues[value][0].has_key(paramName):
                raise RuntimeError("Duplicate param name (%s) found for value '%s'" % (paramName, value))
            self.m_validValues[value][0][paramName] = paramValue

    def GetGroupName(self):
        return self.m_group

    def GetValidValues(self):
        return self.m_validValues

    def HasGroup(self):
        if len(self.m_group) > 0:
            return True
        else:
            return False

    def HasValidValues(self):
        if len(self.m_validValues) > 0:
            return True
        else:
            return False

    def SetGroupName(self, name):
        self.m_group = name