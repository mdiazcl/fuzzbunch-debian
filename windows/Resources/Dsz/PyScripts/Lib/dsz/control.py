# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: control.py
import _dsz

class echo:

    def On():
        _dsz.dszObj.echo_on()

    def Off():
        _dsz.dszObj.echo_off()

    On = staticmethod(On)
    Off = staticmethod(Off)


class flags:

    def Normalize():
        _dsz.dszObj.flags_normalize()

    def Save():
        _dsz.dszObj.flags_save()

    def Restore():
        _dsz.dszObj.flags_restore()

    Normalize = staticmethod(Normalize)
    Save = staticmethod(Save)
    Restore = staticmethod(Restore)


class Method:

    def __init__(self):
        self.Enter()
        self.Stored = True

    def __del__(self):
        if self.Stored:
            self.Stored = False
            self.Exit()

    def __enter__(self):
        if not self.Stored:
            self.Enter()
            self.Stored = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.Stored:
            self.Exit()
            self.Stored = False

    def Enter():
        _dsz.dszObj.flags_save()
        _dsz.dszObj.flags_normalize()

    def Exit():
        _dsz.dszObj.flags_restore()

    Enter = staticmethod(Enter)
    Exit = staticmethod(Exit)


class quiet:

    def On():
        _dsz.dszObj.quiet_on()

    def Off():
        _dsz.dszObj.quiet_off()

    On = staticmethod(On)
    Off = staticmethod(Off)


class wow64:

    def Disable():
        _dsz.dszObj.wow64_disable()

    def Enable():
        _dsz.dszObj.wow64_enable()

    Disable = staticmethod(Disable)
    Enable = staticmethod(Enable)