# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_long.py
"""Fixer that turns 'long' into 'int' everywhere.
"""
from lib2to3 import fixer_base
from lib2to3.fixer_util import is_probably_builtin

class FixLong(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "'long'"

    def transform(self, node, results):
        if is_probably_builtin(node):
            node.value = 'int'
            node.changed()