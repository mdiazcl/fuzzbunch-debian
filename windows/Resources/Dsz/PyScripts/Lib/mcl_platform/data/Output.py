# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Output.py
import _dsz
import mcl.data.DataHandlerInput
import mcl.status
from mcl.data.DataHandlerOutput import DataHandlerOutput

class DszDataHandlerOutput(DataHandlerOutput):

    def __init__(self, input):
        pass

    def End(self):
        pass

    def CreateLogFile(self, prefix, suffix, subDir=None, utf8=True):
        import mcl.data.env
        import os
        import os.path
        _LOG_DIR_ENV_NAME = '_LOGPATH'
        storageDir = mcl.data.env.GetValue(_LOG_DIR_ENV_NAME, True)
        if len(storageDir) > 0:
            storageDir = storageDir + '/'
        if subDir != None:
            storageDir = storageDir + subDir
        try:
            os.makedirs(storageDir)
        except:
            pass

        path = os.path.normpath(storageDir + '/')
        numTrysLeft = 1000
        while numTrysLeft > 0:
            numTrysLeft = numTrysLeft - 1
            logName = _logGenerateName(prefix, suffix)
            fullPath = os.path.normpath(path + '/' + logName)
            if len(fullPath) > 260:
                logName = _logGenerateName('x', suffix)
                fullPath = os.path.normpath(path + '/' + logName)
            try:
                _f = os.open(fullPath, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_BINARY)
                f = os.fdopen(_f, 'wb')
            except:
                import dsz
                dsz.Sleep(10)
                continue

            if utf8:
                f.write('\ufeff')
            return (
             f, path, logName)

        return (None, '', '')

    def GoToBackground(self):
        _dsz.dszObj.go_to_background()

    def RecordXml(self, xml):
        try:
            xml.AddAttribute('dataTimestamp', _dsz.dszObj.dsz_dh_get_collecttime_str())
        except:
            pass

        _dsz.dszObj.xml_store(xml.GetXml())

    def SetTaskStatus(self, status):
        rtn = _dsz.dszObj.dsz_dh_set_status(status)
        if rtn != 0:
            raise RuntimeError('Failed to set command status')

    def Start(self, elementName, namespace, attributes):
        pass

    def TranslateOsError(self, osError):
        return _dsz.dszObj.dsz_dh_error_get_system(osError)


def StartOutput(OutputFilename, input):
    if not isinstance(input, mcl.data.DataHandlerInput.DataHandlerInput):
        raise RuntimeError('input must be of type mcl.data.DataHandlerInput.DataHandlerInput')
    return DszDataHandlerOutput(input)


def _logGenerateName(prefix, suffix):
    import dsz
    import re
    logName = ''
    if prefix != None:
        logName = logName + prefix
    logName = logName + '_' + dsz.Timestamp()
    if suffix != None and len(suffix) > 0:
        logName = logName + '.' + suffix
    logName = re.sub('\\*', '%', logName)
    logName = re.sub('/', '%', logName)
    logName = re.sub('\\\\', '%', logName)
    logName = re.sub(':', '%', logName)
    logName = re.sub('"', '%', logName)
    logName = re.sub('>', '%', logName)
    logName = re.sub('<', '%', logName)
    logName = re.sub('\\|', '%', logName)
    logName = re.sub('\\?', '%', logName)
    logName = re.sub(' ', '%', logName)
    return logName