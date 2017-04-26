# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_xreadlines.py
"""Fix "for x in f.xreadlines()" -> "for x in f".

This fixer will also convert g(f.xreadlines) into g(f.__iter__)."""
from .. import fixer_base
from ..fixer_util import Name

class FixXreadlines(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< call=any+ trailer< '.' 'xreadlines' > trailer< '(' ')' > >\n    |\n    power< any+ trailer< '.' no_call='xreadlines' > >\n    "

    def transform(self, node, results):
        no_call = results.get('no_call')
        if no_call:
            no_call.replace(Name('__iter__', prefix=no_call.prefix))
        else:
            node.replace([ x.clone() for x in results['call'] ])