# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: md5.py
import warnings
warnings.warn('the md5 module is deprecated; use hashlib instead', DeprecationWarning, 2)
from hashlib import md5
new = md5
blocksize = 1
digest_size = 16