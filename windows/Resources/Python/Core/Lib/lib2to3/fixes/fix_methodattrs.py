# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_methodattrs.py
"""Fix bound method attributes (method.im_? -> method.__?__).
"""
from .. import fixer_base
from ..fixer_util import Name
MAP = {'im_func': '__func__',
   'im_self': '__self__',
   'im_class': '__self__.__class__'
   }

class FixMethodattrs(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< any+ trailer< '.' attr=('im_func' | 'im_self' | 'im_class') > any* >\n    "

    def transform(self, node, results):
        attr = results['attr'][0]
        new = unicode(MAP[attr.value])
        attr.replace(Name(new, prefix=attr.prefix))