# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: option.py
import dsky
import dsz
from dsky.menu.item import Item
from dsky.menu.menu import Menu

class Option(Item):

    def __init__(self, text, func, param=None):
        self.text = text
        self.func = func
        self.param = param
        self.isShown = True

    def IsShown(self):
        return self.isShown

    def SetShown(self, bShow):
        self.isShown = bShow

    def IsOption(self):
        return True

    def Display(self, index):
        dsz.ui.Echo(' %2d) %s' % (index, self.text))

    def Execute(self):
        return self.func(self.param)