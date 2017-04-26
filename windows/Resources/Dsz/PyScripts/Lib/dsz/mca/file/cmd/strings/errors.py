# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_UNAVAILABLE_FULLPATH = mcl.status.framework.ERR_START + 1
ERR_UNABLE_TO_OPEN_FILE = mcl.status.framework.ERR_START + 2
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 3
ERR_NO_UNICODE = mcl.status.framework.ERR_START + 4
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_UNAVAILABLE_FULLPATH: 'Unable to get the full path',
   ERR_UNABLE_TO_OPEN_FILE: 'Unable to open file',
   ERR_MARSHAL_FAILED: 'Marshal of return data failed',
   ERR_NO_UNICODE: "This platform doesn't support UNICODE"
   }