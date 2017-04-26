# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: dynOptionMenuWidget.py
"""
OptionMenu widget modified to allow dynamic menu reconfiguration
and setting of highlightthickness
"""
from Tkinter import OptionMenu
from Tkinter import _setit
import copy

class DynOptionMenu(OptionMenu):
    """
    unlike OptionMenu, our kwargs can include highlightthickness
    """

    def __init__(self, master, variable, value, *values, **kwargs):
        kwargsCopy = copy.copy(kwargs)
        if 'highlightthickness' in kwargs.keys():
            del kwargs['highlightthickness']
        OptionMenu.__init__(self, master, variable, value, *values, **kwargs)
        self.config(highlightthickness=kwargsCopy.get('highlightthickness'))
        self.variable = variable
        self.command = kwargs.get('command')

    def SetMenu(self, valueList, value=None):
        """
        clear and reload the menu with a new set of options.
        valueList - list of new options
        value - initial value to set the optionmenu's menubutton to
        """
        self['menu'].delete(0, 'end')
        for item in valueList:
            self['menu'].add_command(label=item, command=_setit(self.variable, item, self.command))

        if value:
            self.variable.set(value)