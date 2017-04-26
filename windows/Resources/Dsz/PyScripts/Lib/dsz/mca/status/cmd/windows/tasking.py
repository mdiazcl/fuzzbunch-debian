# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: tasking.py
import mcl_platform.tasking
from tasking_dsz import *
_fw = mcl_platform.tasking.GetFramework()
if _fw == 'dsz':
    RPC_INFO_LIST_STATIONS = dsz.RPC_INFO_LIST_STATIONS
    RPC_INFO_LIST_WINDOWS = dsz.RPC_INFO_LIST_WINDOWS
    RPC_INFO_SCREENSHOT = dsz.RPC_INFO_SCREENSHOT
    RPC_INFO_CLOSE_WINDOW = dsz.RPC_INFO_CLOSE_WINDOW
    RPC_INFO_LIST_BUTTONS = dsz.RPC_INFO_LIST_BUTTONS
    RPC_INFO_CLICK_BUTTON = dsz.RPC_INFO_CLICK_BUTTON
else:
    raise RuntimeError('Unsupported framework (%s)' % _fw)