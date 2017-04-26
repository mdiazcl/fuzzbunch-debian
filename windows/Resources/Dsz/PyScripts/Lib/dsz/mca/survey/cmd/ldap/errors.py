# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_FUNC_NOT_FOUND = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_EXFIL_FAILED = mcl.status.framework.ERR_START + 3
ERR_QUERY_FAILED = mcl.status.framework.ERR_START + 4
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 5
ERR_INIT_FAILED = mcl.status.framework.ERR_START + 6
ERR_CONNECTION_FAILED = mcl.status.framework.ERR_START + 7
ERR_COM_INIT_FAILED = mcl.status.framework.ERR_START + 8
ERR_SERVER_BIND_FAILED = mcl.status.framework.ERR_START + 9
ERR_SETSEARCH_FAILED = mcl.status.framework.ERR_START + 10
ERR_SEARCH_FAILED = mcl.status.framework.ERR_START + 11
ERR_EXCEPTION_THROWN = mcl.status.framework.ERR_START + 12
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_FUNC_NOT_FOUND: 'Required function is not available',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_EXFIL_FAILED: 'Return of data failed',
   ERR_QUERY_FAILED: 'Query of registry failed',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_INIT_FAILED: 'Initalization failed',
   ERR_CONNECTION_FAILED: 'Connection to LDAP server failed',
   ERR_COM_INIT_FAILED: 'COM Initialization failed',
   ERR_SERVER_BIND_FAILED: 'Bind with LDAP server failed',
   ERR_SETSEARCH_FAILED: 'Setting of Search Preferences failed',
   ERR_SEARCH_FAILED: 'Search failed',
   ERR_EXCEPTION_THROWN: 'Exception thrown'
   }