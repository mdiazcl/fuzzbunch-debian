# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\pyreadline\console\event.py
# Compiled at: 2011-06-23 17:25:54


class Event(object):

    def __init__(self, console, input):
        pass

    def __repr__(self):
        if self.type in ('KeyPress', 'KeyRelease'):
            chr = self.char
            if ord(chr) < ord('A'):
                chr = '?'
            s = "%s char='%s'%d keysym='%s' keycode=%d:%x state=%x keyinfo=%s" % (
             self.type, chr, ord(self.char), self.keysym, self.keycode, self.keycode,
             self.state, self.keyinfo)
        elif self.type in ('Motion', 'Button'):
            s = '%s x=%d y=%d state=%x' % (self.type, self.x, self.y, self.state)
        elif self.type == 'Configure':
            s = '%s w=%d h=%d' % (self.type, self.width, self.height)
        elif self.type in ('FocusIn', 'FocusOut'):
            s = self.type
        elif self.type == 'Menu':
            s = '%s state=%x' % (self.type, self.state)
        else:
            s = 'unknown event type'
        return s