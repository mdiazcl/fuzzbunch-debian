# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_unicode.py
"""Fixer that changes unicode to str, unichr to chr, and u"..." into "...".

"""
import re
from ..pgen2 import token
from .. import fixer_base
_mapping = {'unichr': 'chr','unicode': 'str'}
_literal_re = re.compile('[uU][rR]?[\\\'\\"]')

class FixUnicode(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "STRING | 'unicode' | 'unichr'"

    def transform(self, node, results):
        if node.type == token.NAME:
            new = node.clone()
            new.value = _mapping[node.value]
            return new
        if node.type == token.STRING:
            if _literal_re.match(node.value):
                new = node.clone()
                new.value = new.value[1:]
                return new