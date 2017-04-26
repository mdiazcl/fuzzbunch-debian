# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_OPEN_PROCESS_FAILED = mcl.status.framework.ERR_START + 1
ERR_TERMINATE_PROCESS_FAILED = mcl.status.framework.ERR_START + 2
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_OPEN_PROCESS_FAILED: 'Open of process failed',
   ERR_TERMINATE_PROCESS_FAILED: 'Termination of process failed'
   }