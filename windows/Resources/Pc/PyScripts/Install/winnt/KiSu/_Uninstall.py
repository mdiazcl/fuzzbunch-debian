# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: _Uninstall.py
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
    return demi.windows.module.Uninstall('Pc', demi.registry.PC.Name, demi.registry.PC.Id, ask=False)


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)