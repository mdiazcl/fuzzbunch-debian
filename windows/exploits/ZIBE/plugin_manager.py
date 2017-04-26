# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\plugin_manager.py
# Compiled at: 2013-02-27 18:02:46
from plugins import *

class PluginManager(object):
    __plugins__ = {}
    __handlers__ = {}

    def __init__(self):
        plugins = __import__('ZIBE').plugins
        for member in plugins.__all__:
            plugin_mod = getattr(plugins, member)
            for type_name in dir(plugin_mod):
                try:
                    t = getattr(plugin_mod, type_name)
                    if t.zibe_plugin is True:
                        self._add_plugin(t)
                except AttributeError:
                    pass

    def plugin_commands(self, plugin_name):
        if self.__plugins__.has_key(plugin_name):
            return self.__plugins__[plugin_name].get_command_handlers().keys()
        return None
        return None

    def plugins(self):
        ret = []
        for p in self.__plugins__.keys():
            ret.append((p, self.__plugins__[p].friendly_name))

        return ret

    def _add_plugin(self, t):
        inst = t()
        self.__plugins__[t.plugin_name] = inst
        handlers = inst.get_command_handlers()
        for k in handlers:
            self.__handlers__[k] = handlers[k]

    def handler_exists(self, cmd_name):
        if self.__handlers__.has_key(cmd_name):
            return True
        return False

    def get_handler_info(self, name):
        if self.__handlers__.has_key(name) is False:
            return None
        return self.__handlers__[name]

    def get_handler_func(self, cmd):
        return self.__handlers__[cmd]['handler']

    def invoke_cmd_handler(self, cmd, ctx, stdin, stdout, stderr, args):
        if self.__handlers__.has_key(cmd):
            record = self.__handlers__[cmd]
            return record['handler'](stdin, stdout, stderr, ctx, args)
        raise Exception('No command handler registered under that name')