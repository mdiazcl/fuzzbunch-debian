# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_paren.py
"""Fixer that addes parentheses where they are required

This converts ``[x for x in 1, 2]`` to ``[x for x in (1, 2)]``."""
from .. import fixer_base
from ..fixer_util import LParen, RParen

class FixParen(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n        atom< ('[' | '(')\n            (listmaker< any\n                comp_for<\n                    'for' NAME 'in'\n                    target=testlist_safe< any (',' any)+ [',']\n                     >\n                    [any]\n                >\n            >\n            |\n            testlist_gexp< any\n                comp_for<\n                    'for' NAME 'in'\n                    target=testlist_safe< any (',' any)+ [',']\n                     >\n                    [any]\n                >\n            >)\n        (']' | ')') >\n    "

    def transform(self, node, results):
        target = results['target']
        lparen = LParen()
        lparen.prefix = target.prefix
        target.prefix = ''
        target.insert_child(0, lparen)
        target.append_child(RParen())