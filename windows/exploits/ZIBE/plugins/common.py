# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\plugins\common.py
# Compiled at: 2012-12-12 00:44:46


def zibe_plugin(plugin_name, friendly_name):

    def _zibe_plugin(cls):
        cls.zibe_plugin = True
        cls.plugin_name = plugin_name
        cls.friendly_name = friendly_name
        return cls

    return _zibe_plugin


def command_alias(alias_list):

    def _comand_alias(fnc):
        fnc.alias_list = alias_list
        return fnc

    return _command_alias


def command_hide(is_hidden):

    def _command_hide(fnc):
        fnc.is_hidden = is_hidden
        return fnc

    return _command_hide


def command_help_string(help_string):

    def _command_help_string(fnc):
        fnc.help_string = help_string
        return fnc

    return _command_help_string


def _default_help_handler(help_string):

    def __default_help_handler():
        return help_string

    return __default_help_handler


class ZBCommandPlugin(object):

    def write_line(self, line):
        self.stdout.write(line + '\n')

    def get_command_handlers(self):
        cmds = {}
        for name in dir(self.__class__):
            if name[:3] == 'do_':
                cmd_name = name[3:]
                handler = getattr(self, name)
                try:
                    hidden = handler.is_hidden
                except AttributeError:
                    hidden = False

                help_func = None
                try:
                    help_func = _default_help_handler(handler.help_string)
                except AttributeError:
                    try:
                        help_func = getattr(self, 'help_' + cmd_name)
                    except AttributeError:
                        help_func = _default_help_handler('No help available for this command')

                cmds[cmd_name] = {'handler': handler,'hidden': hidden,'help_func': help_func
                   }
                try:
                    alias_list = handler.alias_list
                    for a in alias_list:
                        cmds[a] = {'handler': handler,'hidden': True,'help_func': None
                           }

                except AttributeError:
                    pass

        return cmds