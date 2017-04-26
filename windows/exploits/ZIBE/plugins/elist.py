# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\plugins\elist.py
# Compiled at: 2013-02-27 18:02:46
from . import common
from ..context_mgr import ZIBEException
from .. import zbutil
import re
import codecs
import logging
ELIST_FILE = 'D:\\DSZOpsDisk\\Resources\\Ep\\elist.txt'
FLAGDICT = {'???': None,
   '!!!': None,
   '+++': None,
   '***': None
   }
EXELIST = None
ELIST_REGEX = re.compile('(?P<exe>[~_\\-A-Za-z0-9\\.\\-\\(\\)\\s\\[\\]\\\\@\\!]+)\\:[\\s\t]*(?P<flags>[\\?!\\+\\*]{3})?(?P<description>[A-Za-z0-9~_\\-\\.\\s]+)(?P=flags)?')

def parse_elist_file(filename):
    d = {}
    with codecs.open(filename, 'rb', 'UTF_16') as fh:
        for l in fh.readlines():
            if l == '\r\n':
                continue
            try:
                m = ELIST_REGEX.match(l)
                flags = m.group('flags')
                if flags is None:
                    flags = ''
                d[m.group('exe').strip().lower()] = (
                 m.group('description').strip().encode('UTF-8'), flags.encode('UTF-8'))
            except AttributeError, e:
                print 'Failure in matching line: {0}'.format(e)
                print "'{0}'".format(l)

    return d


@common.zibe_plugin('elist_services', 'Elist Process Management Plugin')
class ElistServicesPlugin(common.ZBCommandPlugin):

    def __init__(self, *args, **kwargs):
        common.ZBCommandPlugin.__init__(self, *args, **kwargs)
        self.elist = None
        return

    @common.command_help_string('pselist [elist_file] [reg] - List all currently running processes and\n' + "                             check them against the elist.  Use 'reg'\n" + '                             to use the remote registry method instead\n' + '                             of terminal service API')
    def do_pselist(self, stdin, stdout, stderr, ctx, args):
        op = ctx.ENUM_PROC_BY_TS
        if len(args) > 0 and 'reg' in args:
            args.remove('reg')
            op = ctx.ENUM_PROC_BY_WINREG
        if len(args) > 0:
            self.elist = parse_elist_file(args[0])
            print >> stdout, 'Parsed elist file %s' % args[0]
        elif self.elist is None:
            try:
                self.elist = parse_elist_file(ELIST_FILE)
                logging.info('Parsed elist file %s' % ELIST_FILE)
            except Exception, e:
                stderr.write('**************************')
                stderr.write('Elist file is empty: %s' % e)
                stderr.write('**************************')
                self.elist = {}

        try:
            list = ctx.enumerate_processes(op)
        except ZIBEException, err:
            logging.error(str(err))
            return

        if len(list) > 0:
            print >> stdout, ''
            print >> stdout, '%-5s %-25s %-5s %-5s %-7s %-20s %3s %s' % ('Flags', 'Image Name',
                                                                         'PID', 'PPID',
                                                                         'Threads',
                                                                         'Account',
                                                                         '', 'Description')
            print >> stdout, '----- ------------------------- ----- ----- ------- --------------------     ------------------------------'
            for p in sorted(list, key=lambda x: x['pid']):
                if op == ctx.ENUM_PROC_BY_WINREG:
                    eentry = self.elist.get(p['image_name'].lower() + '.exe')
                else:
                    eentry = self.elist.get(p['image_name'].lower())
                if eentry is not None:
                    print >> stdout, '%-5s %-25s %-5d %-5d %-7d %-20s %3s %s' % (eentry[1], p['image_name'][0:30], p['pid'], p['ppid'], p['thread_count'], p['account_name'][0:30], eentry[1], eentry[0])
                else:
                    print >> stdout, '%-5s %-25s %-5d %-5d %-7d %-20s %3s %s' % ('     ', p['image_name'][0:30], p['pid'], p['ppid'], p['thread_count'], p['account_name'][0:30], '', '')

        else:
            print >> stdout, 'No processes returned!  This is probably an error'
        return