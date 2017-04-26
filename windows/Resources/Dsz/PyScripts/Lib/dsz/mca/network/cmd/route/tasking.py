# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: tasking.py
import mcl_platform.tasking
from tasking_dsz import *
from tasking_ur import *
_fw = mcl_platform.tasking.GetFramework()
if _fw == 'dsz':
    RPC_INFO_QUERY = dsz.RPC_INFO_QUERY
    RPC_INFO_ADD = dsz.RPC_INFO_ADD
    RPC_INFO_DELETE = dsz.RPC_INFO_DELETE
elif _fw == 'ur':
    RPC_INFO_QUERY = ur.RPC_INFO_QUERY
    RPC_INFO_ADD = ur.RPC_INFO_ADD
    RPC_INFO_DELETE = ur.RPC_INFO_DELETE
else:
    raise RuntimeError('Unsupported framework (%s)' % _fw)