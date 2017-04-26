# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_basestring.py
"""Fixer for basestring -> str."""
from .. import fixer_base
from ..fixer_util import Name

class FixBasestring(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "'basestring'"

    def transform(self, node, results):
        return Name('str', prefix=node.prefix)