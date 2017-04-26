# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_repr.py
"""Fixer that transforms `xyzzy` into repr(xyzzy)."""
from .. import fixer_base
from ..fixer_util import Call, Name, parenthesize

class FixRepr(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              atom < '`' expr=any '`' >\n              "

    def transform(self, node, results):
        expr = results['expr'].clone()
        if expr.type == self.syms.testlist1:
            expr = parenthesize(expr)
        return Call(Name('repr'), [expr], prefix=node.prefix)