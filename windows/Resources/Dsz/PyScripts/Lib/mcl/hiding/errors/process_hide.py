# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: process_hide.py
ERR_PROCESS_HIDE_SUCCESS = 0
ERR_PROCESS_HIDE_UNSUPPORTED_PLATFORM = 1
ERR_PROCESS_HIDE_INVALID_PARAMS = 2
ERR_PROCESS_HIDE_PROCESS_NOT_FOUND = 3
ERR_PROCESS_HIDE_INVALID_LINKS = 4
ERR_PROCESS_HIDE_SYSTEM_NOT_FOUND = 5
ERR_PROCESS_HIDE_EXCEPTION = 6
ERR_PROCESS_HIDE_NOT_HIDDEN = 7
ERR_PROCESS_HIDE_INVALID_LOCATION = 8
errorStrings = {ERR_PROCESS_HIDE_UNSUPPORTED_PLATFORM: 'Unsupported platform',
   ERR_PROCESS_HIDE_INVALID_PARAMS: 'Invalid parameters sent to process elevation procedure',
   ERR_PROCESS_HIDE_PROCESS_NOT_FOUND: 'Process not found',
   ERR_PROCESS_HIDE_INVALID_LINKS: 'Invalid process links found in EPROCESS',
   ERR_PROCESS_HIDE_SYSTEM_NOT_FOUND: 'Unable to find SYSTEM process',
   ERR_PROCESS_HIDE_EXCEPTION: 'Exception thrown hiding process',
   ERR_PROCESS_HIDE_NOT_HIDDEN: 'Process is not hidden',
   ERR_PROCESS_HIDE_INVALID_LOCATION: 'Invalid EPROCESS location for given ID'
   }