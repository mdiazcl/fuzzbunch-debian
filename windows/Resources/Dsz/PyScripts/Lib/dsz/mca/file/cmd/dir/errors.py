# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_DONE_MAX_ENTRIES = mcl.status.framework.ERR_START + 1
ERR_GET_FULL_PATH_FAILED = mcl.status.framework.ERR_START + 2
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 3
ERR_ENUM_FAILED = mcl.status.framework.ERR_START + 4
ERR_SEND_FAILED = mcl.status.framework.ERR_START + 5
ERR_EXCEPTION = mcl.status.framework.ERR_START + 6
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_DONE_MAX_ENTRIES: 'Directory listing completed due to exceeding maximum entries',
   ERR_GET_FULL_PATH_FAILED: 'Failed to get full path',
   ERR_MARSHAL_FAILED: 'Error marshaling data',
   ERR_ENUM_FAILED: 'Directory listing failed',
   ERR_SEND_FAILED: 'Failed to send back data',
   ERR_EXCEPTION: 'Encountered an exception'
   }