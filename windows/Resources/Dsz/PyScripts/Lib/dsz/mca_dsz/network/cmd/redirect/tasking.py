# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: tasking.py
import mcl_platform.tasking
from tasking_dsz import *
_fw = mcl_platform.tasking.GetFramework()
if _fw == 'dsz':
    RPC_INFO_LISTEN = dsz.RPC_INFO_LISTEN
    RPC_INFO_CONNECT = dsz.RPC_INFO_CONNECT
    RPC_INFO_COMMAND = dsz.RPC_INFO_COMMAND
    RPC_INFO_WAIT = dsz.RPC_INFO_WAIT
else:
    raise RuntimeError('Unsupported framework (%s)' % _fw)