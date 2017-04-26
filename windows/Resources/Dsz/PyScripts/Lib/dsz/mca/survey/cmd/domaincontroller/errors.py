# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_ENUM_FAILED = mcl.status.framework.ERR_START + 2
ERR_NO_SERVER_ENUM_DATA = mcl.status.framework.ERR_START + 3
ERR_NO_ENTRIES = mcl.status.framework.ERR_START + 4
ERR_DC_NOT_FOUND = mcl.status.framework.ERR_START + 5
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_ENUM_FAILED: 'Enumeration of servers failed',
   ERR_NO_SERVER_ENUM_DATA: 'No data obtained for domain controllers',
   ERR_NO_ENTRIES: 'No dc entries found',
   ERR_DC_NOT_FOUND: 'All methods for determining domain controllers failed'
   }