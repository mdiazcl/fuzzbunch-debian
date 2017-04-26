# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import _dsz
import sys

def Background():
    if _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    return _dsz.dszObj.go_to_background()


def Echo(str, type=_dsz.dszObj.DEFAULT, checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    _dsz.dszObj.echo(str, type)


def GetString(userPrompt, defaultValue='', checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    return _dsz.dszObj.get_string(userPrompt, defaultValue)


def GetInt(userPrompt, defaultValue='', checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    return _dsz.dszObj.get_int(userPrompt, defaultValue)


def Pause(str='', checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    _dsz.dszObj.pause(str)


def Prompt(str, defaultToYes=True, checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    return _dsz.dszObj.prompt(str, defaultToYes)