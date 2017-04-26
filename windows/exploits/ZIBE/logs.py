# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\logs.py
# Compiled at: 2013-02-27 18:02:46
import sys
import logging
import binascii
import zbutil

class ZIBEOutputFormatter(logging.Formatter):

    def format(self, record):
        msg = record.getMessage()
        printable = all(map(lambda x: zbutil.isprint(x, linefeeds=True), record.getMessage()))
        if printable:
            return msg
        return zbutil.hexdump(msg)


def get_logger(logfile='debug.log'):
    logging.addLevelName(5, 'COMMAND')
    level = 5
    logger = logging.getLogger()
    logger.setLevel(level)
    if logfile is not None:
        fh = logging.FileHandler(logfile, mode='w')
        fh.setLevel(level)
        fhFormatter = ZIBEOutputFormatter('[%(levelname)-8s] %(filename)-18s (line %(lineno)-4s) -- %(message)s')
        fh.setFormatter(fhFormatter)
        logger.addHandler(fh)
    return logger