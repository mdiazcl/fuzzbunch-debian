# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz

def DisableCommand(command, addr=dsz.script.Env['target_address']):
    return _processCommand('disable', command, addr)


def PromptCommand(command, addr=dsz.script.Env['target_address']):
    return _processCommand('prompt', command, addr)


def _processCommand(action, command, addr):
    if addr == dsz.script.Env['local_address']:
        location = 'local'
    elif addr == dsz.script.Env['target_address']:
        location = 'current'
    else:
        location = 'any'
    x = dsz.control.Method()
    dsz.control.echo.Off()
    return dsz.cmd.Run('%s %s %s' % (action, command, location))