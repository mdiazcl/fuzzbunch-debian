# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: _PromptCommand.py
import dsz
import sys

def main():
    dsz.control.quiet.Off()
    try:
        cmdId = int(sys.argv[1])
        cmdName = dsz.cmd.data.Get('CommandMetaData::Name', dsz.TYPE_STRING, cmdId=cmdId, checkForStop=False)[0]
    except:
        cmdName = 'Unknown (cmdId=%s)' % sys.argv[1]

    return dsz.ui.Prompt("Do you want to run '%s'?" % cmdName, defaultToYes=True)


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)