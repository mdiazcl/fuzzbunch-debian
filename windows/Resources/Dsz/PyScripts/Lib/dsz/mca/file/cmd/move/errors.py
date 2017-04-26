# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_GET_FULL_PATH_FAILED = mcl.status.framework.ERR_START + 1
ERR_MOVE_FAILED = mcl.status.framework.ERR_START + 2
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 3
ERR_MOVE_PATH_UNC_AFTER_REBOOT = mcl.status.framework.ERR_START + 4
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_GET_FULL_PATH_FAILED: 'Failed to get full paths for move',
   ERR_MOVE_FAILED: 'Failed to move file',
   ERR_MARSHAL_FAILED: 'Failed to marshal output',
   ERR_MOVE_PATH_UNC_AFTER_REBOOT: 'Cannot do move-after-reboot action with network paths.'
   }