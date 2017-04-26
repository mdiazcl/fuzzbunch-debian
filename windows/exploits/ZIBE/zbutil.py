# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\zbutil.py
# Compiled at: 2013-02-27 16:22:28
import shlex
import binascii
import array
import ctypes
import sys
languagemap = {'english': 'english-us',
   'russian': 'russian',
   'chinese-simplified': 'chinese-simplified',
   'chinese-traditional': 'chinese-traditional',
   'korean': 'korean',
   'german': 'german',
   'czech': 'czech',
   'utf8': ''
   }
if sys.platform == 'Win32':

    def i18nized(fn):

        def wrap(self, *args, **kwargs):
            if self.language != 'English':
                try:
                    ctypes.cdll.msvcrt.setlocale(0, ctypes.c_char_p(languagemap[self.language]))
                except:
                    pass

            ret = self.fn(*args, **kwargs)
            ctypes.cdll.msvcrt.setlocale(0, ctypes.c_char_p(languagemap['english']))
            return ret

        return wrap


else:

    def i18nized(fn):

        @functools.wraps(fn)
        def wrap(self, *args, **kwargs):
            return self.fn(*args, **kwargs)

        return wrap


def arg_to_utf8(value):
    type = value[:2]
    if type == 'L:':
        value = value[2:].encode('utf-16le')
        value = unicode(value, 'UTF-16le')
    elif type == 'A:':
        value = value[2:].encode('utf-8')
    elif type == 'H:':
        value = binascii.unhexlify(value[2:])
    else:
        try:
            value = binascii.unhexlify(value).decode('utf-16le')
        except:
            try:
                value = value.decode('utf-8')
            except:
                raise

    return value.encode('UTF-8')


def rolling_xor(str, key):
    a = array.array('H', str)
    key = int(key)
    result = map(lambda x: (x ^ key) & 65535, a)
    keystr = binascii.unhexlify(''.join(map(lambda x: '%.04x' % x, result)))
    return keystr


def parseargs(arg):
    if len(arg) > 0:
        args = shlex.split(arg, False, False)
        for i in xrange(0, len(args)):
            if args[i][0] == '"' and args[i][-1] == '"' or args[i][0] == "'" and args[i][-1] == "'":
                args[i] = args[i][1:-1]

    else:
        args = []
    return args


def arg2value(arg, size=None):
    if isinstance(arg, str):
        if arg[:2] == '0x':
            value = int(arg[2:], 16)
        else:
            value = int(arg)
        return value
    if isinstance(arg, list):
        if all(map(lambda x: isinstance(x, int), arg)):
            string = ''.join(map(lambda x: '%.02x' % x, arg))
        elif all(map(lambda x: isinstance(x, str), arg)):
            string = ''.join(map(lambda x: '%.02x' % int(x, 16), arg))
        else:
            raise ValueError('Invalid list format for conversion')
        value = binascii.unhexlify(string)
    else:
        raise ValueError("Invalid type %s to 'tohexstring'" % str(type(arg)))
    if size is not None and len(str(value)) > size:
        raise ValueError("Invalid value specified for the type's size limit")
    return value


def isprint(x, linefeeds=False):
    val = int(binascii.hexlify(x), 16)
    printable = val >= 32 and val <= 126
    if linefeeds:
        printable = printable or val == 13 or val == 10
    return printable


def isprintable(string, linefeeds=True):
    return all(map(lambda x: isprint(x, linefeeds=linefeeds), string))


def hexdump(buff, width=8, sep=6):
    rows = len(buff) / width
    rest = len(buff) % width
    string = ''
    for i in xrange(rows):
        string += ' '.join(map(lambda x: binascii.hexlify(x), buff[i * width:i * width + width]))
        string += ' ' * sep
        string += ''.join(map(lambda x: (str(x) if isprint(x) else '.'), buff[i * width:i * width + width]))
        string += '\n'

    string += ' '.join(map(lambda x: binascii.hexlify(x), buff[rows * width:]))
    string += '   ' * (width - rest)
    string += ' ' * sep
    string += ''.join(map(lambda x: (str(x) if isprint(x) else '.'), buff[rows * width:]))
    return string


def hexdump_short(buff, width=8, sep=6):
    if len(buff) < width:
        b = buff
        rest = width - len(buff)
    else:
        b = buff[:width]
        rest = 0
    string = ''
    string += ' '.join(map(lambda x: binascii.hexlify(x), b))
    string += '   ' * rest + ' ' * sep
    string += ''.join(map(lambda x: (str(x) if isprint(x) else '.'), b))
    if len(buff) > len(b):
        string += '     (%d bytes suppressed)' % (len(buff) - len(b))
    return string


def asciidump(buff):
    return ''.join(map(lambda x: (str(x) if isprint(x, linefeeds=True) else '.'), buff))


missing = object()

class OrderedDict(dict):

    def __init__(self, *args, **kwargs):
        dict.__init__(self)
        self._keys = []
        self.update(*args, **kwargs)

    def __delitem__(self, key):
        dict.__delitem__(self, key)
        self._keys.remove(key)

    def __setitem__(self, key, item):
        if key not in self:
            self._keys.append(key)
        dict.__setitem__(self, key, item)

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}
        d = memo.get(id(self), missing)
        if d is not missing:
            return d
        memo[id(self)] = d = self.__class__()
        dict.__init__(d, deepcopy(self.items(), memo))
        d._keys = self._keys[:]
        return d

    def __getstate__(self):
        return {'items': dict(self),'keys': self._keys}

    def __setstate__(self, d):
        self._keys = d['keys']
        dict.update(d['items'])

    def __reversed__(self):
        return reversed(self._keys)

    def __eq__(self, other):
        if isinstance(other, odict):
            if not dict.__eq__(self, other):
                return False
            return self.items() == other.items()
        return dict.__eq__(self, other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __cmp__(self, other):
        if isinstance(other, odict):
            return cmp(self.items(), other.items())
        if isinstance(other, dict):
            return dict.__cmp__(self, other)
        return NotImplemented

    @classmethod
    def fromkeys(cls, iterable, default=None):
        return cls(((key, default) for key in iterable))

    def clear(self):
        del self._keys[:]
        dict.clear(self)

    def copy(self):
        return self.__class__(self)

    def items(self):
        return zip(self._keys, self.values())

    def iteritems(self):
        return izip(self._keys, self.itervalues())

    def keys(self):
        return self._keys[:]

    def iterkeys(self):
        return iter(self._keys)

    def pop(self, key, default=missing):
        if default is missing:
            return dict.pop(self, key)
        if key not in self:
            return default
        self._keys.remove(key)
        return dict.pop(self, key, default)

    def popitem(self, key):
        self._keys.remove(key)
        return dict.popitem(key)

    def setdefault(self, key, default=None):
        if key not in self:
            self._keys.append(key)
        dict.setdefault(self, key, default)

    def update(self, *args, **kwargs):
        sources = []
        if len(args) == 1:
            if hasattr(args[0], 'iteritems'):
                sources.append(args[0].iteritems())
            else:
                sources.append(iter(args[0]))
        elif args:
            raise TypeError('expected at most one positional argument')
        if kwargs:
            sources.append(kwargs.iteritems())
        for iterable in sources:
            for key, val in iterable:
                self[key] = val

    def values(self):
        return map(self.get, self._keys)

    def itervalues(self):
        return map(self.get, self._keys)

    def index(self, item):
        return self._keys.index(item)

    def byindex(self, item):
        key = self._keys[item]
        return (
         key, dict.__getitem__(self, key))

    def reverse(self):
        self._keys.reverse()

    def sort(self, *args, **kwargs):
        self._keys.sort(*args, **kwargs)

    def __repr__(self):
        return 'odict.odict(%r)' % self.items()

    __copy__ = copy
    __iter__ = iterkeys