# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_ws_comma.py
"""Fixer that changes 'a ,b' into 'a, b'.

This also changes '{a :b}' into '{a: b}', but does not touch other
uses of colons.  It does not touch other uses of whitespace.

"""
from .. import pytree
from ..pgen2 import token
from .. import fixer_base

class FixWsComma(fixer_base.BaseFix):
    explicit = True
    PATTERN = "\n    any<(not(',') any)+ ',' ((not(',') any)+ ',')* [not(',') any]>\n    "
    COMMA = pytree.Leaf(token.COMMA, ',')
    COLON = pytree.Leaf(token.COLON, ':')
    SEPS = (COMMA, COLON)

    def transform(self, node, results):
        new = node.clone()
        comma = False
        for child in new.children:
            if child in self.SEPS:
                prefix = child.prefix
                if prefix.isspace() and '\n' not in prefix:
                    child.prefix = ''
                comma = True
            else:
                if comma:
                    prefix = child.prefix
                    if not prefix:
                        child.prefix = ' '
                comma = False

        return new