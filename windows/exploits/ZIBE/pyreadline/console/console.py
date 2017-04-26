# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\pyreadline\console\console.py
# Compiled at: 2011-10-07 02:48:04
import sys
import os
import traceback
import re
import pyreadline.unicode_helper as unicode_helper
from pyreadline.logger import log
from pyreadline.unicode_helper import ensure_unicode, ensure_str
from pyreadline.keysyms import make_KeyPress, KeyPress
from pyreadline.console.ansi import AnsiState, AnsiWriter
try:
    import ctypes.util
    from ctypes import *
    from _ctypes import call_function
    from ctypes.wintypes import *
except ImportError:
    raise ImportError('You need ctypes to run this code')

def nolog(string):
    pass


log = nolog
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
ENABLE_WINDOW_INPUT = 8
ENABLE_MOUSE_INPUT = 16
ENABLE_PROCESSED_INPUT = 1
WHITE = 7
BLACK = 0
MENU_EVENT = 8
KEY_EVENT = 1
MOUSE_MOVED = 1
MOUSE_EVENT = 2
WINDOW_BUFFER_SIZE_EVENT = 4
FOCUS_EVENT = 16
MENU_EVENT = 8
VK_SHIFT = 16
VK_CONTROL = 17
VK_MENU = 18
GENERIC_READ = int(2147483648)
GENERIC_WRITE = 1073741824

class COORD(Structure):
    _fields_ = [
     (
      'X', c_short),
     (
      'Y', c_short)]


class SMALL_RECT(Structure):
    _fields_ = [
     (
      'Left', c_short),
     (
      'Top', c_short),
     (
      'Right', c_short),
     (
      'Bottom', c_short)]


class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    _fields_ = [
     (
      'dwSize', COORD),
     (
      'dwCursorPosition', COORD),
     (
      'wAttributes', c_short),
     (
      'srWindow', SMALL_RECT),
     (
      'dwMaximumWindowSize', COORD)]


class CHAR_UNION(Union):
    _fields_ = [
     (
      'UnicodeChar', c_wchar),
     (
      'AsciiChar', c_char)]


class CHAR_INFO(Structure):
    _fields_ = [
     (
      'Char', CHAR_UNION),
     (
      'Attributes', c_short)]


class KEY_EVENT_RECORD(Structure):
    _fields_ = [
     (
      'bKeyDown', c_byte),
     (
      'pad2', c_byte),
     (
      'pad1', c_short),
     (
      'wRepeatCount', c_short),
     (
      'wVirtualKeyCode', c_short),
     (
      'wVirtualScanCode', c_short),
     (
      'uChar', CHAR_UNION),
     (
      'dwControlKeyState', c_int)]


class MOUSE_EVENT_RECORD(Structure):
    _fields_ = [
     (
      'dwMousePosition', COORD),
     (
      'dwButtonState', c_int),
     (
      'dwControlKeyState', c_int),
     (
      'dwEventFlags', c_int)]


class WINDOW_BUFFER_SIZE_RECORD(Structure):
    _fields_ = [
     (
      'dwSize', COORD)]


class MENU_EVENT_RECORD(Structure):
    _fields_ = [
     (
      'dwCommandId', c_uint)]


class FOCUS_EVENT_RECORD(Structure):
    _fields_ = [
     (
      'bSetFocus', c_byte)]


class INPUT_UNION(Union):
    _fields_ = [
     (
      'KeyEvent', KEY_EVENT_RECORD),
     (
      'MouseEvent', MOUSE_EVENT_RECORD),
     (
      'WindowBufferSizeEvent', WINDOW_BUFFER_SIZE_RECORD),
     (
      'MenuEvent', MENU_EVENT_RECORD),
     (
      'FocusEvent', FOCUS_EVENT_RECORD)]


class INPUT_RECORD(Structure):
    _fields_ = [
     (
      'EventType', c_short),
     (
      'Event', INPUT_UNION)]


class CONSOLE_CURSOR_INFO(Structure):
    _fields_ = [
     (
      'dwSize', c_int),
     (
      'bVisible', c_byte)]


funcs = [
 'AllocConsole',
 'CreateConsoleScreenBuffer',
 'FillConsoleOutputAttribute',
 'FillConsoleOutputCharacterW',
 'FreeConsole',
 'GetConsoleCursorInfo',
 'GetConsoleMode',
 'GetConsoleScreenBufferInfo',
 'GetConsoleTitleW',
 'GetProcAddress',
 'GetStdHandle',
 'PeekConsoleInputW',
 'ReadConsoleInputW',
 'ScrollConsoleScreenBufferW',
 'SetConsoleActiveScreenBuffer',
 'SetConsoleCursorInfo',
 'SetConsoleCursorPosition',
 'SetConsoleMode',
 'SetConsoleScreenBufferSize',
 'SetConsoleTextAttribute',
 'SetConsoleTitleW',
 'SetConsoleWindowInfo',
 'WriteConsoleW',
 'WriteConsoleOutputCharacterW',
 'WriteFile']
key_modifiers = {VK_SHIFT: 1,VK_CONTROL: 1,
   VK_MENU: 1,
   91: 1
   }

def split_block(text, size=1000):
    return [ text[start:start + size] for start in range(0, len(text), size) ]


class Console(object):

    def __init__(self, newbuffer=0):
        if newbuffer:
            self.hout = self.CreateConsoleScreenBuffer(GENERIC_READ | GENERIC_WRITE, 0, None, 1, None)
            self.SetConsoleActiveScreenBuffer(self.hout)
        else:
            self.hout = self.GetStdHandle(STD_OUTPUT_HANDLE)
        self.hin = self.GetStdHandle(STD_INPUT_HANDLE)
        self.inmode = DWORD(0)
        self.GetConsoleMode(self.hin, byref(self.inmode))
        self.SetConsoleMode(self.hin, 15)
        info = CONSOLE_SCREEN_BUFFER_INFO()
        self.GetConsoleScreenBufferInfo(self.hout, byref(info))
        self.attr = info.wAttributes
        self.saveattr = info.wAttributes
        self.defaultstate = AnsiState()
        self.defaultstate.winattr = info.wAttributes
        self.ansiwriter = AnsiWriter(self.defaultstate)
        background = self.attr & 240
        for escape in self.escape_to_color:
            if self.escape_to_color[escape] is not None:
                self.escape_to_color[escape] |= background

        log('initial attr=%x' % self.attr)
        self.softspace = 0
        self.serial = 0
        self.pythondll = CDLL('python%s%s' % (sys.version[0], sys.version[2]))
        self.pythondll.PyMem_Malloc.restype = c_size_t
        self.pythondll.PyMem_Malloc.argtypes = [c_size_t]
        self.inputHookPtr = c_void_p.from_address(addressof(self.pythondll.PyOS_InputHook)).value
        setattr(Console, 'PyMem_Malloc', self.pythondll.PyMem_Malloc)
        return

    def __del__(self):
        self.SetConsoleTextAttribute(self.hout, self.saveattr)
        self.SetConsoleMode(self.hin, self.inmode)
        self.FreeConsole()

    def _get_top_bot(self):
        info = CONSOLE_SCREEN_BUFFER_INFO()
        self.GetConsoleScreenBufferInfo(self.hout, byref(info))
        rect = info.srWindow
        top = rect.Top
        bot = rect.Bottom
        return (
         top, bot)

    def fixcoord(self, x, y):
        if x < 0 or y < 0:
            info = CONSOLE_SCREEN_BUFFER_INFO()
            self.GetConsoleScreenBufferInfo(self.hout, byref(info))
            if x < 0:
                x = info.srWindow.Right - x
                y = info.srWindow.Bottom + y
        return c_int(y << 16 | x)

    def pos(self, x=None, y=None):
        if x is None:
            info = CONSOLE_SCREEN_BUFFER_INFO()
            self.GetConsoleScreenBufferInfo(self.hout, byref(info))
            return (
             info.dwCursorPosition.X, info.dwCursorPosition.Y)
        return self.SetConsoleCursorPosition(self.hout, self.fixcoord(x, y))
        return

    def home(self):
        self.pos(0, 0)

    terminal_escape = re.compile('(\x01?\x1b\\[[0-9;]+m\x02?)')
    escape_parts = re.compile('\x01?\x1b\\[([0-9;]+)m\x02?')
    escape_to_color = {'0;30': 0,'0;31': 4,
       '0;32': 2,
       '0;33': 6,
       '0;34': 1,
       '0;35': 5,
       '0;36': 6,
       '0;37': 7,
       '1;30': 7,
       '1;31': 12,
       '1;32': 10,
       '1;33': 14,
       '1;34': 9,
       '1;35': 13,
       '1;36': 11,
       '1;37': 15,
       '0': None
       }
    motion_char_re = re.compile('([\n\r\t\x08\x07])')

    def write_scrolling(self, text, attr=None):
        x, y = self.pos()
        w, h = self.size()
        scroll = 0
        chunks = self.motion_char_re.split(text)
        for chunk in chunks:
            n = self.write_color(chunk, attr)
            if len(chunk) == 1:
                if chunk[0] == '\n':
                    x = 0
                    y += 1
                else:
                    if chunk[0] == '\r':
                        x = 0
                    elif chunk[0] == '\t':
                        x = 8 * (int(x / 8) + 1)
                        if x > w:
                            x -= w
                            y += 1
                    elif chunk[0] == '\x07':
                        pass
                    elif chunk[0] == '\x08':
                        x -= 1
                        if x < 0:
                            y -= 1
                    else:
                        x += 1
                    if x == w:
                        x = 0
                        y += 1
                if y == h:
                    scroll += 1
                    y = h - 1
            else:
                x += n
                l = int(x / w)
                x = x % w
                y += l
                if y >= h:
                    scroll += y - h + 1
                    y = h - 1

        return scroll

    def write_color(self, text, attr=None):
        text = ensure_unicode(text)
        n, res = self.ansiwriter.write_color(text, attr)
        junk = DWORD(0)
        for attr, chunk in res:
            log('console.attr:%s' % unicode(attr))
            log('console.chunk:%s' % unicode(chunk))
            self.SetConsoleTextAttribute(self.hout, attr.winattr)
            for short_chunk in split_block(chunk):
                self.WriteConsoleW(self.hout, short_chunk, len(short_chunk), byref(junk), None)

        return n

    def write_plain(self, text, attr=None):
        text = ensure_unicode(text)
        log('write("%s", %s)' % (text, attr))
        if attr is None:
            attr = self.attr
        junk = DWORD(0)
        self.SetConsoleTextAttribute(self.hout, attr)
        for short_chunk in split_block(chunk):
            self.WriteConsoleW(self.hout, ensure_unicode(short_chunk), len(short_chunk), byref(junk), None)

        return len(text)

    if os.environ.has_key('EMACS'):

        def write_color(self, text, attr=None):
            text = ensure_str(text)
            junk = DWORD(0)
            self.WriteFile(self.hout, text, len(text), byref(junk), None)
            return len(text)

        write_plain = write_color

    def write(self, text):
        text = ensure_unicode(text)
        log('write("%s")' % text)
        return self.write_color(text)

    def isatty(self):
        return True

    def flush(self):
        pass

    def page(self, attr=None, fill=' '):
        if attr is None:
            attr = self.attr
        if len(fill) != 1:
            raise ValueError
        info = CONSOLE_SCREEN_BUFFER_INFO()
        self.GetConsoleScreenBufferInfo(self.hout, byref(info))
        if info.dwCursorPosition.X != 0 or info.dwCursorPosition.Y != 0:
            self.SetConsoleCursorPosition(self.hout, self.fixcoord(0, 0))
        w = info.dwSize.X
        n = DWORD(0)
        for y in range(info.dwSize.Y):
            self.FillConsoleOutputAttribute(self.hout, attr, w, self.fixcoord(0, y), byref(n))
            self.FillConsoleOutputCharacterW(self.hout, ord(fill[0]), w, self.fixcoord(0, y), byref(n))

        self.attr = attr
        return

    def text(self, x, y, text, attr=None):
        if attr is None:
            attr = self.attr
        pos = self.fixcoord(x, y)
        n = DWORD(0)
        self.WriteConsoleOutputCharacterW(self.hout, text, len(text), pos, byref(n))
        self.FillConsoleOutputAttribute(self.hout, attr, n, pos, byref(n))
        return

    def clear_to_end_of_window(self):
        top, bot = self._get_top_bot()
        pos = self.pos()
        w, h = self.size()
        self.rectangle((pos[0], pos[1], w, pos[1] + 1))
        if pos[1] < bot:
            self.rectangle((0, pos[1] + 1, w, bot + 1))

    def rectangle(self, rect, attr=None, fill=' '):
        x0, y0, x1, y1 = rect
        n = DWORD(0)
        if attr is None:
            attr = self.attr
        for y in range(y0, y1):
            pos = self.fixcoord(x0, y)
            self.FillConsoleOutputAttribute(self.hout, attr, x1 - x0, pos, byref(n))
            self.FillConsoleOutputCharacterW(self.hout, ord(fill[0]), x1 - x0, pos, byref(n))

        return

    def scroll(self, rect, dx, dy, attr=None, fill=' '):
        if attr is None:
            attr = self.attr
        x0, y0, x1, y1 = rect
        source = SMALL_RECT(x0, y0, x1 - 1, y1 - 1)
        dest = self.fixcoord(x0 + dx, y0 + dy)
        style = CHAR_INFO()
        style.Char.AsciiChar = ensure_str(fill[0])
        style.Attributes = attr
        return self.ScrollConsoleScreenBufferW(self.hout, byref(source), byref(source), dest, byref(style))

    def scroll_window(self, lines):
        info = CONSOLE_SCREEN_BUFFER_INFO()
        self.GetConsoleScreenBufferInfo(self.hout, byref(info))
        rect = info.srWindow
        log('sw: rtop=%d rbot=%d' % (rect.Top, rect.Bottom))
        top = rect.Top + lines
        bot = rect.Bottom + lines
        h = bot - top
        maxbot = info.dwSize.Y - 1
        if top < 0:
            top = 0
            bot = h
        if bot > maxbot:
            bot = maxbot
            top = bot - h
        nrect = SMALL_RECT()
        nrect.Top = top
        nrect.Bottom = bot
        nrect.Left = rect.Left
        nrect.Right = rect.Right
        log('sn: top=%d bot=%d' % (top, bot))
        r = self.SetConsoleWindowInfo(self.hout, True, byref(nrect))
        log('r=%d' % r)

    def get(self):
        inputHookFunc = c_void_p.from_address(self.inputHookPtr).value
        Cevent = INPUT_RECORD()
        count = DWORD(0)
        while 1:
            if inputHookFunc:
                call_function(inputHookFunc, ())
            status = self.ReadConsoleInputW(self.hin, byref(Cevent), 1, byref(count))
            if status and count.value == 1:
                e = event(self, Cevent)
                return e

    def getkeypress(self):
        while 1:
            e = self.get()
            if e.type == 'KeyPress' and e.keycode not in key_modifiers:
                log('console.getkeypress %s' % e)
                if e.keyinfo.keyname == 'next':
                    self.scroll_window(12)
                elif e.keyinfo.keyname == 'prior':
                    self.scroll_window(-12)
                else:
                    return e
            elif e.type == 'KeyRelease' and e.keyinfo == KeyPress('S', False, True, False, 'S'):
                log('getKeypress:%s,%s,%s' % (e.keyinfo, e.keycode, e.type))
                return e

    def getchar(self):
        Cevent = INPUT_RECORD()
        count = DWORD(0)
        while 1:
            status = self.ReadConsoleInputW(self.hin, byref(Cevent), 1, byref(count))
            if status and count.value == 1 and Cevent.EventType == 1 and Cevent.Event.KeyEvent.bKeyDown:
                sym = keysym(Cevent.Event.KeyEvent.wVirtualKeyCode)
                if len(sym) == 0:
                    sym = Cevent.Event.KeyEvent.uChar.AsciiChar
                return sym

    def peek(self):
        Cevent = INPUT_RECORD()
        count = DWORD(0)
        status = self.PeekConsoleInputW(self.hin, byref(Cevent), 1, byref(count))
        if status and count == 1:
            return event(self, Cevent)

    def title(self, txt=None):
        if txt:
            self.SetConsoleTitleW(txt)
        else:
            buffer = create_unicode_buffer(200)
            n = self.GetConsoleTitleW(buffer, 200)
            if n > 0:
                return buffer.value[:n]

    def size(self, width=None, height=None):
        info = CONSOLE_SCREEN_BUFFER_INFO()
        status = self.GetConsoleScreenBufferInfo(self.hout, byref(info))
        if not status:
            return
        if width is not None and height is not None:
            wmin = info.srWindow.Right - info.srWindow.Left + 1
            hmin = info.srWindow.Bottom - info.srWindow.Top + 1
            width = max(width, wmin)
            height = max(height, hmin)
            self.SetConsoleScreenBufferSize(self.hout, self.fixcoord(width, height))
        else:
            return (
             info.dwSize.X, info.dwSize.Y)
        return

    def cursor(self, visible=None, size=None):
        info = CONSOLE_CURSOR_INFO()
        if self.GetConsoleCursorInfo(self.hout, byref(info)):
            if visible is not None:
                info.bVisible = visible
            if size is not None:
                info.dwSize = size
            self.SetConsoleCursorInfo(self.hout, byref(info))
        return

    def bell(self):
        self.write('\x07')

    def next_serial(self):
        self.serial += 1
        return self.serial


for func in funcs:
    setattr(Console, func, getattr(windll.kernel32, func))

if sys.version_info[:2] < (2, 6):
    msvcrt = cdll.msvcrt
else:
    msvcrt = cdll.LoadLibrary(ctypes.util.find_msvcrt())
_strncpy = msvcrt.strncpy
_strncpy.restype = c_char_p
_strncpy.argtypes = [c_char_p, c_char_p, c_size_t]
_strdup = msvcrt._strdup
_strdup.restype = c_char_p
_strdup.argtypes = [c_char_p]
LPVOID = c_void_p
LPCVOID = c_void_p
FARPROC = c_void_p
LPDWORD = POINTER(DWORD)
Console.AllocConsole.restype = BOOL
Console.AllocConsole.argtypes = []
Console.CreateConsoleScreenBuffer.restype = HANDLE
Console.CreateConsoleScreenBuffer.argtypes = [DWORD, DWORD, c_void_p, DWORD, LPVOID]
Console.FillConsoleOutputAttribute.restype = BOOL
Console.FillConsoleOutputAttribute.argtypes = [HANDLE, WORD, DWORD, c_int, LPDWORD]
Console.FillConsoleOutputCharacterW.restype = BOOL
Console.FillConsoleOutputCharacterW.argtypes = [HANDLE, c_ushort, DWORD, c_int, LPDWORD]
Console.FreeConsole.restype = BOOL
Console.FreeConsole.argtypes = []
Console.GetConsoleCursorInfo.restype = BOOL
Console.GetConsoleCursorInfo.argtypes = [HANDLE, c_void_p]
Console.GetConsoleMode.restype = BOOL
Console.GetConsoleMode.argtypes = [HANDLE, LPDWORD]
Console.GetConsoleScreenBufferInfo.restype = BOOL
Console.GetConsoleScreenBufferInfo.argtypes = [HANDLE, c_void_p]
Console.GetConsoleTitleW.restype = DWORD
Console.GetConsoleTitleW.argtypes = [c_wchar_p, DWORD]
Console.GetProcAddress.restype = FARPROC
Console.GetProcAddress.argtypes = [HMODULE, c_char_p]
Console.GetStdHandle.restype = HANDLE
Console.GetStdHandle.argtypes = [DWORD]
Console.PeekConsoleInputW.restype = BOOL
Console.PeekConsoleInputW.argtypes = [HANDLE, c_void_p, DWORD, LPDWORD]
Console.ReadConsoleInputW.restype = BOOL
Console.ReadConsoleInputW.argtypes = [HANDLE, c_void_p, DWORD, LPDWORD]
Console.ScrollConsoleScreenBufferW.restype = BOOL
Console.ScrollConsoleScreenBufferW.argtypes = [HANDLE, c_void_p, c_void_p, c_int, c_void_p]
Console.SetConsoleActiveScreenBuffer.restype = BOOL
Console.SetConsoleActiveScreenBuffer.argtypes = [HANDLE]
Console.SetConsoleCursorInfo.restype = BOOL
Console.SetConsoleCursorInfo.argtypes = [HANDLE, c_void_p]
Console.SetConsoleCursorPosition.restype = BOOL
Console.SetConsoleCursorPosition.argtypes = [HANDLE, c_int]
Console.SetConsoleMode.restype = BOOL
Console.SetConsoleMode.argtypes = [HANDLE, DWORD]
Console.SetConsoleScreenBufferSize.restype = BOOL
Console.SetConsoleScreenBufferSize.argtypes = [HANDLE, c_int]
Console.SetConsoleTextAttribute.restype = BOOL
Console.SetConsoleTextAttribute.argtypes = [HANDLE, WORD]
Console.SetConsoleTitleW.restype = BOOL
Console.SetConsoleTitleW.argtypes = [c_wchar_p]
Console.SetConsoleWindowInfo.restype = BOOL
Console.SetConsoleWindowInfo.argtypes = [HANDLE, BOOL, c_void_p]
Console.WriteConsoleW.restype = BOOL
Console.WriteConsoleW.argtypes = [HANDLE, c_void_p, DWORD, LPDWORD, LPVOID]
Console.WriteConsoleOutputCharacterW.restype = BOOL
Console.WriteConsoleOutputCharacterW.argtypes = [HANDLE, c_wchar_p, DWORD, c_int, LPDWORD]
Console.WriteFile.restype = BOOL
Console.WriteFile.argtypes = [HANDLE, LPCVOID, DWORD, LPDWORD, c_void_p]
from event import Event
VkKeyScan = windll.user32.VkKeyScanA

class event(Event):

    def __init__(self, console, input):
        self.type = '??'
        self.serial = console.next_serial()
        self.width = 0
        self.height = 0
        self.x = 0
        self.y = 0
        self.char = ''
        self.keycode = 0
        self.keysym = '??'
        self.keyinfo = None
        self.width = None
        if input.EventType == KEY_EVENT:
            if input.Event.KeyEvent.bKeyDown:
                self.type = 'KeyPress'
            else:
                self.type = 'KeyRelease'
            self.char = input.Event.KeyEvent.uChar.UnicodeChar
            self.keycode = input.Event.KeyEvent.wVirtualKeyCode
            self.state = input.Event.KeyEvent.dwControlKeyState
            self.keyinfo = make_KeyPress(self.char, self.state, self.keycode)
        elif input.EventType == MOUSE_EVENT:
            if input.Event.MouseEvent.dwEventFlags & MOUSE_MOVED:
                self.type = 'Motion'
            else:
                self.type = 'Button'
            self.x = input.Event.MouseEvent.dwMousePosition.X
            self.y = input.Event.MouseEvent.dwMousePosition.Y
            self.state = input.Event.MouseEvent.dwButtonState
        elif input.EventType == WINDOW_BUFFER_SIZE_EVENT:
            self.type = 'Configure'
            self.width = input.Event.WindowBufferSizeEvent.dwSize.X
            self.height = input.Event.WindowBufferSizeEvent.dwSize.Y
        elif input.EventType == FOCUS_EVENT:
            if input.Event.FocusEvent.bSetFocus:
                self.type = 'FocusIn'
            else:
                self.type = 'FocusOut'
        elif input.EventType == MENU_EVENT:
            self.type = 'Menu'
            self.state = input.Event.MenuEvent.dwCommandId
        return


def getconsole(buffer=1):
    c = Console(buffer)
    return c


HOOKFUNC22 = CFUNCTYPE(c_char_p, c_char_p)
HOOKFUNC23 = CFUNCTYPE(c_char_p, c_void_p, c_void_p, c_char_p)
readline_hook = None
readline_ref = None

def hook_wrapper_23(stdin, stdout, prompt):
    global readline_hook
    try:
        res = ensure_str(readline_hook(prompt))
        if res and not isinstance(res, str):
            raise TypeError, 'readline must return a string.'
    except KeyboardInterrupt:
        return 0
    except EOFError:
        res = ''
    except:
        print >> sys.stderr, 'Readline internal error'
        traceback.print_exc()
        res = '\n'

    n = len(res)
    p = Console.PyMem_Malloc(n + 1)
    _strncpy(cast(p, c_char_p), res, n + 1)
    return p


def hook_wrapper(prompt):
    try:
        res = ensure_str(readline_hook(prompt))
        if res and not isinstance(res, str):
            raise TypeError, 'readline must return a string.'
    except KeyboardInterrupt:
        return 0
    except EOFError:
        res = ''
    except:
        print >> sys.stderr, 'Readline internal error'
        traceback.print_exc()
        res = '\n'

    p = _strdup(res)
    return p


def install_readline(hook):
    global readline_hook
    global readline_ref
    readline_hook = hook
    PyOS_RFP = c_void_p.from_address(Console.GetProcAddress(sys.dllhandle, 'PyOS_ReadlineFunctionPointer'))
    if sys.version < '2.3':
        readline_ref = HOOKFUNC22(hook_wrapper)
    else:
        readline_ref = HOOKFUNC23(hook_wrapper_23)
    func_start = c_void_p.from_address(addressof(readline_ref)).value
    PyOS_RFP.value = func_start


if __name__ == '__main__':
    import time
    import sys

    def p(char):
        return chr(VkKeyScan(ord(char)) & 255)


    c = Console(0)
    sys.stdout = c
    sys.stderr = c
    c.page()
    print p('d'), p('D')
    c.pos(5, 10)
    c.write('hi there')
    print 'some printed output'
    for i in range(10):
        q = c.getkeypress()
        print q

    del c