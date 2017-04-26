# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: tasking_ur.py
import mcl.framework
import mcl.tasking

class ur:
    MODULE_ID = 34818
    RPC_INFO_QUERY = mcl.tasking.RpcInfo(mcl.framework.UR, [MODULE_ID, 1])
    RPC_INFO_ADD = mcl.tasking.RpcInfo(mcl.framework.UR, [MODULE_ID, 2])
    RPC_INFO_DELETE = mcl.tasking.RpcInfo(mcl.framework.UR, [MODULE_ID, 3])