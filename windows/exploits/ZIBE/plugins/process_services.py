# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\plugins\process_services.py
# Compiled at: 2013-02-27 18:02:46
from . import common
from ..context_mgr import ZIBEException
from .. import zbutil
import logging

@common.zibe_plugin('process_services', 'Process Management Plugin')
class ProcessServicesPlugin(common.ZBCommandPlugin):

    def help_pslist(self):
        return '\n'.join(['pslist [reg] - List all currently running processes.',
         '               The default method is to use the TS API.',
         '               Use reg to use the remote registry',
         ''])

    def do_pslist(self, stdin, stdout, stderr, ctx, args):
        op = ctx.ENUM_PROC_BY_TS
        if len(args) > 0 and args[0].lower() == 'reg':
            op = ctx.ENUM_PROC_BY_WINREG
        try:
            list = ctx.enumerate_processes(op)
        except ZIBEException, err:
            print >> stderr, str(err)
            return

        if len(list) > 0:
            print >> stdout, '%-25s %-5s %-5s %-7s %-20s' % ('Image Name', 'PID', 'PPID',
                                                             'Threads', 'Account')
            print >> stdout, '------------------------- ----- ----- ------- --------------------'
            for p in sorted(list, key=lambda x: x['pid']):
                print >> stdout, '%-25s %-5d %-5d %-7d %-30s' % (p['image_name'][0:30], p['pid'], p['ppid'], p['thread_count'], p['account_name'][0:30])

        else:
            print >> stderr, 'No processes returned!'

    @common.command_help_string('pskill <pid> - Kills the specified process. This command cannot kill system processes')
    def do_pskill(self, stdin, stdout, stderr, ctx, args):
        if len(args) != 1:
            print >> stderr, 'The syntax of the command is incorrect'
            return
        try:
            pid = int(args[0])
        except TypeError:
            print >> stderr, 'Invalid PID'
            return

        try:
            ctx.kill_process(pid)
        except ZIBEException, err:
            print >> stderr, str(err)
            return

        print >> stdout, 'Successfully killed process %d' % pid