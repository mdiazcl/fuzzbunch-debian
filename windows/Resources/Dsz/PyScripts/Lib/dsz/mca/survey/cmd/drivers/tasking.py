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
    RPC_INFO_LOAD = dsz.RPC_INFO_LOAD
    RPC_INFO_UNLOAD = dsz.RPC_INFO_UNLOAD
else:
    raise RuntimeError('Unsupported framework (%s)' % _fw)