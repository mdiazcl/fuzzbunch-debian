# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_KERNEL_MODE_NULL = mcl.status.framework.ERR_START + 2
ERR_RUN_IN_KERNEL_MODE = mcl.status.framework.ERR_START + 3
ERR_PHYS_MEMORY_MAP = mcl.status.framework.ERR_START + 4
ERR_PRIV_API = mcl.status.framework.ERR_START + 5
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_KERNEL_MODE_NULL: 'Function pointer to RunInKernelMode is null',
   ERR_RUN_IN_KERNEL_MODE: 'Function findAddress failed. Could not get access to physical memory. ',
   ERR_PHYS_MEMORY_MAP: 'Unable to map physical memory',
   ERR_PRIV_API: 'Unable to get Privlege API'
   }