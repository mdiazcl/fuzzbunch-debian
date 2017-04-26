# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: _Upgrade.py
import dsz
import dsz.lp
dsz.lp.AddResDirToPath('DeMi')
import demi
import demi.windows.module
import glob
import os
import re
import shutil
import sys

def main():
    dsz.control.echo.Off()
    localFile = sys.argv[1]
    procName = sys.argv[2]
    upgradedFromNewer = demi.windows.module.Upgrade('Pc', localFile, 'wshtcpip', demi.registry.PC.Id, ask=False)
    if not upgradedFromNewer:
        dsz.ui.Echo('    NOT FOUND, Must retry with older name...', dsz.GOOD)
    return upgradedFromNewer or demi.windows.module.Upgrade('Pc', localFile, 'PC', demi.registry.PC.Id, ask=False)


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)