# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_CREATE_FAILED = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_GET_FULL_PATH_FAILED = mcl.status.framework.ERR_START + 2
ERR_INVALID_PARAM = mcl.status.framework.ERR_START + 3
errorStrings = {ERR_CREATE_FAILED: 'Failed to create directory',
   ERR_MARSHAL_FAILED: 'Error marshaling data',
   ERR_GET_FULL_PATH_FAILED: 'Error obtaining absolute path',
   ERR_INVALID_PARAM: 'Invalid parameter'
   }