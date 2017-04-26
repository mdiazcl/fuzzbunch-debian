# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: tasking.py
import mcl_platform.tasking
from tasking_dsz import *
_fw = mcl_platform.tasking.GetFramework()
if _fw == 'dsz':
    RPC_INFO_LIST = dsz.RPC_INFO_LIST
    RPC_INFO_CONNECT = dsz.RPC_INFO_CONNECT
    RPC_INFO_CONFIG = dsz.RPC_INFO_CONFIG
    RPC_INFO_ADD_MODULE = dsz.RPC_INFO_ADD_MODULE
    RPC_INFO_DELETE_MODULE = dsz.RPC_INFO_DELETE_MODULE
    RPC_INFO_READ_MODULE = dsz.RPC_INFO_READ_MODULE
    RPC_INFO_LOAD_DRIVER = dsz.RPC_INFO_LOAD_DRIVER
    RPC_INFO_UNLOAD_DRIVER = dsz.RPC_INFO_UNLOAD_DRIVER
    RPC_INFO_LOAD_MODULE = dsz.RPC_INFO_LOAD_MODULE
    RPC_INFO_FREE_MODULE = dsz.RPC_INFO_FREE_MODULE
    RPC_INFO_PROCESS_LOAD = dsz.RPC_INFO_PROCESS_LOAD
else:
    raise RuntimeError('Unsupported framework (%s)' % _fw)