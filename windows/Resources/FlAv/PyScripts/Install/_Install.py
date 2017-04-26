# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: _Install.py
import dsz
import dsz.lp
import dsz.menu
import dsz.user
import datetime
import socket
import sys
import xml.dom.minidom
Driver = 'driver'
Method = 'method'

def main():
    dsz.control.echo.Off()
    cmdParams = dsz.lp.cmdline.ParseCommandLine(sys.argv, '_FlAv.txt')
    if len(cmdParams) == 0:
        return False
    else:
        if Method in cmdParams:
            method = '-method %s' % cmdParams[Method][0]
        else:
            method = ''
        if not dsz.cmd.Run('python _FlAv.py -args "-action install -quiet %s"' % method):
            return False
        if not dsz.cmd.Run('python _FlAv.py -args "-action load -quiet %s"' % method):
            return False
        return True


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)