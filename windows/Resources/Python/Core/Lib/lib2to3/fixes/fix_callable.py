# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_callable.py
"""Fixer for callable().

This converts callable(obj) into isinstance(obj, collections.Callable), adding a
collections import if needed."""
from lib2to3 import fixer_base
from lib2to3.fixer_util import Call, Name, String, Attr, touch_import

class FixCallable(fixer_base.BaseFix):
    BM_compatible = True
    order = 'pre'
    PATTERN = "\n    power< 'callable'\n           trailer< lpar='('\n                    ( not(arglist | argument<any '=' any>) func=any\n                      | func=arglist<(not argument<any '=' any>) any ','> )\n                    rpar=')' >\n           after=any*\n    >\n    "

    def transform(self, node, results):
        func = results['func']
        touch_import(None, 'collections', node=node)
        args = [
         func.clone(), String(', ')]
        args.extend(Attr(Name('collections'), Name('Callable')))
        return Call(Name('isinstance'), args, prefix=node.prefix)