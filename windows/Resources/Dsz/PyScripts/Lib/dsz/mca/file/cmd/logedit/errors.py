# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_GET_FULL_PATH_FAILED = mcl.status.framework.ERR_START + 2
ERR_OPENFILE_FAILED = mcl.status.framework.ERR_START + 3
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 4
ERR_WRITE_FILE_FAILED = mcl.status.framework.ERR_START + 5
ERR_UNICODE_NOT_SUPPORTED = mcl.status.framework.ERR_START + 6
ERR_NO_GOOD_LINES_FOUND = mcl.status.framework.ERR_START + 7
ERR_NO_MATCHING_LINES_FOUND = mcl.status.framework.ERR_START + 8
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GET_FULL_PATH_FAILED: 'Get of full file path failed',
   ERR_OPENFILE_FAILED: 'Open of file failed',
   ERR_ALLOC_FAILED: 'Memory allocation failed',
   ERR_WRITE_FILE_FAILED: 'Write to file failed',
   ERR_UNICODE_NOT_SUPPORTED: 'Unicode is not supported on this platform',
   ERR_NO_GOOD_LINES_FOUND: 'No good lines found for replacement of bad lines',
   ERR_NO_MATCHING_LINES_FOUND: 'No lines found with the given phrase'
   }