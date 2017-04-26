# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: _FinalizePayload.py
import dsz
import pc.payload.settings
import sys

def main():
    if len(sys.argv) != 2:
        dsz.ui.Echo('Usage: %s <payloadFile>' % sys.argv[0], dsz.ERROR)
        return False
    return pc.payload.settings.Finalize(sys.argv[1])


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)