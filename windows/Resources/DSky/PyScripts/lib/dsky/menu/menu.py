# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: menu.py
import dsky.menu
import dsz

class Menu(object):

    def __init__(self, title):
        self.title = title
        self.items = list()
        self.header = None
        return

    def SetHeader(self, header):
        self.header = header

    def AddItem(self, item):
        self.items.append(item)

    def RemoveItem(self, item):
        self.items.remove(item)

    def Display(self):
        dsz.ui.Echo(self.title)
        if self.header != None:
            dsz.ui.Echo('')
            self.header.Display()
            dsz.ui.Echo('')
        dsz.ui.Echo(' 0) Exit')
        index = 1
        options = dict()
        for item in self.items:
            if not item.IsShown():
                continue
            item.Display(index)
            if item.IsOption():
                options[index] = item
                index = index + 1

        return options

    def Execute(self):
        if len(self.items) == 0:
            return None
        else:
            while True:
                options = self.Display()
                for i in range(0, 10):
                    choice = dsz.ui.GetInt('Enter the desired option')
                    if choice == 0:
                        return None
                    try:
                        if choice in options:
                            return options[choice].Execute()
                        dsz.ui.Echo('* %d is not a valid option.' % choice, dsz.ERROR)
                    except:
                        raise

            return None

    def ExecuteUntilQuit(self):
        while self.Execute() != None:
            dsz.ui.Pause()

        return