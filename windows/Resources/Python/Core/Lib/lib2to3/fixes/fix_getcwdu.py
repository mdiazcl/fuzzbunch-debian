# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_getcwdu.py
"""
Fixer that changes os.getcwdu() to os.getcwd().
"""
from .. import fixer_base
from ..fixer_util import Name

class FixGetcwdu(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              power< 'os' trailer< dot='.' name='getcwdu' > any* >\n              "

    def transform(self, node, results):
        name = results['name']
        name.replace(Name('getcwd', prefix=name.prefix))