# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_CALLBACK_FAILED = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 3
ERR_LOGON_USER_FAILED = mcl.status.framework.ERR_START + 4
ERR_IMPERSONATE_FAILED = mcl.status.framework.ERR_START + 5
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_CALLBACK_FAILED: 'Error making callback',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_LOGON_USER_FAILED: 'Could not logon the user specified',
   ERR_IMPERSONATE_FAILED: 'Could not impersonate the user specified'
   }