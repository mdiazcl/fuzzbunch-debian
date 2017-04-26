# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_UNABLE_TO_CONVERT = mcl.status.framework.ERR_START
ERR_UNABLE_TO_GET_DST_INFO = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_REMOTE_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 3
ERR_INVALID_PARAMETERS = mcl.status.framework.ERR_START + 4
ERR_WMI_INIT_FAILED = mcl.status.framework.ERR_START + 5
ERR_REMOTE_QUERY_FAILED = mcl.status.framework.ERR_START + 6
errorStrings = {ERR_UNABLE_TO_CONVERT: 'Failed to convert native time to MclTime',
   ERR_UNABLE_TO_GET_DST_INFO: 'Failed to get DST information',
   ERR_MARSHAL_FAILED: 'Data marshal failed',
   ERR_REMOTE_NOT_IMPLEMENTED: 'Remote time not supported on this platform',
   ERR_INVALID_PARAMETERS: 'Invalid parameters',
   ERR_WMI_INIT_FAILED: 'WMI failed to initialize',
   ERR_REMOTE_QUERY_FAILED: 'Query of remote system failed'
   }