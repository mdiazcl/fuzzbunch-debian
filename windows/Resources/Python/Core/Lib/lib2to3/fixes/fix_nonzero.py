# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_nonzero.py
"""Fixer for __nonzero__ -> __bool__ methods."""
from .. import fixer_base
from ..fixer_util import Name, syms

class FixNonzero(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    classdef< 'class' any+ ':'\n              suite< any*\n                     funcdef< 'def' name='__nonzero__'\n                              parameters< '(' NAME ')' > any+ >\n                     any* > >\n    "

    def transform(self, node, results):
        name = results['name']
        new = Name('__bool__', prefix=name.prefix)
        name.replace(new)