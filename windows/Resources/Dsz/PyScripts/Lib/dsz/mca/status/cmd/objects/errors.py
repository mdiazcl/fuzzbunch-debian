# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_GET_FUNCTION_FAILED = mcl.status.framework.ERR_START + 3
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 4
ERR_QUERY_FAILED = mcl.status.framework.ERR_START + 5
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_FUNCTION_FAILED: 'Failed to get required function',
   ERR_ALLOC_FAILED: 'Failed to allocate memory',
   ERR_QUERY_FAILED: 'Unable to query directory (bad syntax or object was not a directory)'
   }