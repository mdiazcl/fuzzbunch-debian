# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 1
ERR_GET_IP_TABLE_FAILED = mcl.status.framework.ERR_START + 2
ERR_GET_ARP_TABLE_FAILED = mcl.status.framework.ERR_START + 3
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 4
ERR_MEMORY_ALLOC_FAILED = mcl.status.framework.ERR_START + 5
ERR_CALLBACK_FAILED = mcl.status.framework.ERR_START + 6
ERR_INVALID_RANGE = mcl.status.framework.ERR_START + 7
ERR_SEND_FAILED = mcl.status.framework.ERR_START + 8
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_GET_IP_TABLE_FAILED: 'Failed to get IP table',
   ERR_GET_ARP_TABLE_FAILED: 'Failed to get ARP table',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_MEMORY_ALLOC_FAILED: 'Memory alloc failed',
   ERR_CALLBACK_FAILED: 'Return of data failed',
   ERR_INVALID_RANGE: 'Invalid IP address range',
   ERR_SEND_FAILED: 'Arp send was not successful'
   }