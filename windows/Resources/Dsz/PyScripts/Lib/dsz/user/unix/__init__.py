# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz

def IsRoot():
    try:
        user = dsz.process.GetCurrent()
        return user == 'root'
    except:
        pass

    return False