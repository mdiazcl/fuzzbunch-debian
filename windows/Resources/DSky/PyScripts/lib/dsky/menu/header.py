# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: header.py
import dsky
import dsz
from dsky.menu.item import Item

class SectionHeader(Item):

    def __init__(self, text):
        self.text = text

    def IsOption(self):
        return False

    def Display(self, index):
        dsz.ui.Echo('')
        dsz.ui.Echo('%s' % self.text)


class MenuHeader(object):

    def __init__(self, func, params=None):
        self.func = func
        self.params = params

    def Display(self):
        if self.params == None:
            self.func()
        else:
            self.func(self.params)
        return