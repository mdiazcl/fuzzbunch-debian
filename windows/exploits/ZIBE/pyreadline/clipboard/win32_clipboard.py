# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\pyreadline\clipboard\win32_clipboard.py
# Compiled at: 2011-06-23 17:25:54
from ctypes import *
from pyreadline.keysyms.winconstants import CF_TEXT, GHND
from pyreadline.unicode_helper import ensure_unicode, ensure_str
OpenClipboard = windll.user32.OpenClipboard
OpenClipboard.argtypes = [c_int]
EmptyClipboard = windll.user32.EmptyClipboard
GetClipboardData = windll.user32.GetClipboardData
GetClipboardData.argtypes = [c_int]
GetClipboardFormatName = windll.user32.GetClipboardFormatNameA
GetClipboardFormatName.argtypes = [c_uint, c_char_p, c_int]
SetClipboardData = windll.user32.SetClipboardData
SetClipboardData.argtypes = [c_int, c_int]
EnumClipboardFormats = windll.user32.EnumClipboardFormats
EnumClipboardFormats.argtypes = [c_int]
CloseClipboard = windll.user32.CloseClipboard
CloseClipboard.argtypes = []
GlobalAlloc = windll.kernel32.GlobalAlloc
GlobalLock = windll.kernel32.GlobalLock
GlobalLock.argtypes = [c_int]
GlobalUnlock = windll.kernel32.GlobalUnlock
GlobalUnlock.argtypes = [c_int]
memcpy = cdll.msvcrt.memcpy

def enum():
    OpenClipboard(0)
    q = EnumClipboardFormats(0)
    while q:
        q = EnumClipboardFormats(q)

    CloseClipboard()


def getformatname(format):
    buffer = c_buffer(' ' * 100)
    bufferSize = sizeof(buffer)
    OpenClipboard(0)
    GetClipboardFormatName(format, buffer, bufferSize)
    CloseClipboard()
    return buffer.value


def GetClipboardText():
    text = ''
    if OpenClipboard(0):
        hClipMem = GetClipboardData(CF_TEXT)
        if hClipMem:
            GlobalLock.restype = c_char_p
            text = GlobalLock(hClipMem)
            GlobalUnlock(hClipMem)
        CloseClipboard()
    return ensure_unicode(text)


def SetClipboardText(text):
    buffer = c_buffer(ensure_str(text))
    bufferSize = sizeof(buffer)
    hGlobalMem = GlobalAlloc(c_int(GHND), c_int(bufferSize))
    GlobalLock.restype = c_void_p
    lpGlobalMem = GlobalLock(c_int(hGlobalMem))
    memcpy(lpGlobalMem, addressof(buffer), c_int(bufferSize))
    GlobalUnlock(c_int(hGlobalMem))
    if OpenClipboard(0):
        EmptyClipboard()
        SetClipboardData(c_int(CF_TEXT), c_int(hGlobalMem))
        CloseClipboard()


if __name__ == '__main__':
    txt = GetClipboardText()
    print txt