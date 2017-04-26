# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: fix_execfile.py
"""Fixer for execfile.

This converts usages of the execfile function into calls to the built-in
exec() function.
"""
from .. import fixer_base
from ..fixer_util import Comma, Name, Call, LParen, RParen, Dot, Node, ArgList, String, syms

class FixExecfile(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< 'execfile' trailer< '(' arglist< filename=any [',' globals=any [',' locals=any ] ] > ')' > >\n    |\n    power< 'execfile' trailer< '(' filename=any ')' > >\n    "

    def transform(self, node, results):
        filename = results['filename']
        globals = results.get('globals')
        locals = results.get('locals')
        execfile_paren = node.children[-1].children[-1].clone()
        open_args = ArgList([filename.clone()], rparen=execfile_paren)
        open_call = Node(syms.power, [Name('open'), open_args])
        read = [Node(syms.trailer, [Dot(), Name('read')]),
         Node(syms.trailer, [LParen(), RParen()])]
        open_expr = [open_call] + read
        filename_arg = filename.clone()
        filename_arg.prefix = ' '
        exec_str = String("'exec'", ' ')
        compile_args = open_expr + [Comma(), filename_arg, Comma(), exec_str]
        compile_call = Call(Name('compile'), compile_args, '')
        args = [
         compile_call]
        if globals is not None:
            args.extend([Comma(), globals.clone()])
        if locals is not None:
            args.extend([Comma(), locals.clone()])
        return Call(Name('exec'), args, prefix=node.prefix)