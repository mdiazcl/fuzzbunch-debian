# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_imports2.py
"""Fix incompatible imports and module references that must be fixed after
fix_imports."""
from . import fix_imports
MAPPING = {'whichdb': 'dbm',
   'anydbm': 'dbm'
   }

class FixImports2(fix_imports.FixImports):
    run_order = 7
    mapping = MAPPING