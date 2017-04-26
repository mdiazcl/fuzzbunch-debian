# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Delegator.py


class Delegator:

    def __init__(self, delegate=None):
        self.delegate = delegate
        self.__cache = {}

    def __getattr__(self, name):
        attr = getattr(self.delegate, name)
        setattr(self, name, attr)
        self.__cache[name] = attr
        return attr

    def resetcache(self):
        for key in self.__cache.keys():
            try:
                delattr(self, key)
            except AttributeError:
                pass

        self.__cache.clear()

    def cachereport(self):
        keys = self.__cache.keys()
        keys.sort()
        print keys

    def setdelegate(self, delegate):
        self.resetcache()
        self.delegate = delegate

    def getdelegate(self):
        return self.delegate