# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\readline.py
# Compiled at: 2011-06-23 17:25:54
from pyreadline.rlmain import Readline
__all__ = [
 'parse_and_bind',
 'get_line_buffer',
 'insert_text',
 'clear_history',
 'read_init_file',
 'read_history_file',
 'write_history_file',
 'get_current_history_length',
 'get_history_length',
 'get_history_item',
 'set_history_length',
 'set_startup_hook',
 'set_pre_input_hook',
 'set_completer',
 'get_completer',
 'get_begidx',
 'get_endidx',
 'set_completer_delims',
 'get_completer_delims',
 'add_history',
 'callback_handler_install',
 'callback_handler_remove',
 'callback_read_char']
rl = Readline()
if rl.disable_readline:

    def dummy(completer=''):
        pass


    for funk in __all__:
        globals()[funk] = dummy

else:

    def GetOutputFile():
        return rl.console


    __all__.append('GetOutputFile')
    import pyreadline.console as console
    read_init_file = rl.read_init_file
    parse_and_bind = rl.parse_and_bind
    clear_history = rl.clear_history
    add_history = rl.add_history
    insert_text = rl.insert_text
    write_history_file = rl.write_history_file
    read_history_file = rl.read_history_file
    get_completer_delims = rl.get_completer_delims
    get_current_history_length = rl.get_current_history_length
    get_history_length = rl.get_history_length
    get_history_item = rl.get_history_item
    get_line_buffer = rl.get_line_buffer
    set_completer = rl.set_completer
    get_completer = rl.get_completer
    get_begidx = rl.get_begidx
    get_endidx = rl.get_endidx
    set_completer_delims = rl.set_completer_delims
    set_history_length = rl.set_history_length
    set_pre_input_hook = rl.set_pre_input_hook
    set_startup_hook = rl.set_startup_hook
    callback_handler_install = rl.callback_handler_install
    callback_handler_remove = rl.callback_handler_remove
    callback_read_char = rl.callback_read_char
    console.install_readline(rl.readline)
__all__.append('rl')