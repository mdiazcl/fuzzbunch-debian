# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_funcattrs.py
"""Fix function attribute names (f.func_x -> f.__x__)."""
from .. import fixer_base
from ..fixer_util import Name

class FixFuncattrs(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< any+ trailer< '.' attr=('func_closure' | 'func_doc' | 'func_globals'\n                                  | 'func_name' | 'func_defaults' | 'func_code'\n                                  | 'func_dict') > any* >\n    "

    def transform(self, node, results):
        attr = results['attr'][0]
        attr.replace(Name('__%s__' % attr.value[5:], prefix=attr.prefix))