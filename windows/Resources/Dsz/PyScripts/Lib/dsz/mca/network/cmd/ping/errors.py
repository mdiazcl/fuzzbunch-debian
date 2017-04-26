# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_CREATE_SOCKET_FAILED = mcl.status.framework.ERR_START + 2
ERR_BINDING_SOCKET_FAILED = mcl.status.framework.ERR_START + 3
ERR_SET_BROADCAST_OPTION_FAILED = mcl.status.framework.ERR_START + 4
ERR_RESOLVE_ADDRESS_FAILED = mcl.status.framework.ERR_START + 5
ERR_SEND_FAILED = mcl.status.framework.ERR_START + 6
ERR_REPLY_TIMEOUT = mcl.status.framework.ERR_START + 7
ERR_RECEIVING_REPLY = mcl.status.framework.ERR_START + 8
ERR_SETUP_FOR_REPLY_FAILED = mcl.status.framework.ERR_START + 9
ERR_GETTING_SRC_ADDR = mcl.status.framework.ERR_START + 10
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 11
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_CREATE_SOCKET_FAILED: 'Error creating the socket',
   ERR_BINDING_SOCKET_FAILED: 'Error binding the socket',
   ERR_SET_BROADCAST_OPTION_FAILED: 'Error setting socket to broadcast mode',
   ERR_RESOLVE_ADDRESS_FAILED: 'Unable to resolve given address',
   ERR_SEND_FAILED: 'Error occured while attempting to send the ping',
   ERR_REPLY_TIMEOUT: 'Timed out while waiting for ping response',
   ERR_RECEIVING_REPLY: 'Error occured while attempting to receive the ping response',
   ERR_SETUP_FOR_REPLY_FAILED: 'Setup for ping replies failed',
   ERR_GETTING_SRC_ADDR: 'Unable to find a source address for ping',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform'
   }