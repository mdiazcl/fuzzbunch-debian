# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\pyreadline\unicode_helper.py
# Compiled at: 2011-06-23 17:25:54
import sys
try:
    pyreadline_codepage = sys.stdout.encoding
except AttributeError:
    pyreadline_codepage = 'ascii'

if pyreadline_codepage is None:
    pyreadline_codepage = 'ascii'

def ensure_unicode(text):
    if isinstance(text, str):
        try:
            return text.decode(pyreadline_codepage, 'replace')
        except (LookupError, TypeError):
            return text.decode('ascii', 'replace')

    return text


def ensure_str(text):
    if isinstance(text, unicode):
        try:
            return text.encode(pyreadline_codepage, 'replace')
        except (LookupError, TypeError):
            return text.encode('ascii', 'replace')

    return text