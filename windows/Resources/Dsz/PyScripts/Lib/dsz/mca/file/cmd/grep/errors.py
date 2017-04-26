# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_GET_FULL_PATH_FAILED = mcl.status.framework.ERR_START + 2
ERR_CALLBACK_FAILED = mcl.status.framework.ERR_START + 3
ERR_ENUM_FAILED = mcl.status.framework.ERR_START + 4
ERR_DONE_MAX_ENTRIES = mcl.status.framework.ERR_START + 5
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 6
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_FULL_PATH_FAILED: 'Unable to get full path',
   ERR_CALLBACK_FAILED: 'Return of data failed',
   ERR_ENUM_FAILED: 'Failed to enumerate given directory',
   ERR_DONE_MAX_ENTRIES: 'Maximum entries exceeded',
   ERR_NOT_IMPLEMENTED: 'Feature not implemented on this platform'
   }