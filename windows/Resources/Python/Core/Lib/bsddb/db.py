# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: db.py
import sys
absolute_import = sys.version_info[0] >= 3
if not absolute_import:
    if __name__.startswith('bsddb3.'):
        from _pybsddb import *
        from _pybsddb import __version__
    else:
        from _bsddb import *
        from _bsddb import __version__
elif __name__.startswith('bsddb3.'):
    exec 'from ._pybsddb import *'
    exec 'from ._pybsddb import __version__'
else:
    exec 'from ._bsddb import *'
    exec 'from ._bsddb import __version__'