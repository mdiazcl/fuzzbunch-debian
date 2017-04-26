# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\plugins\sam.py
# Compiled at: 2013-02-27 18:02:46
from . import common
from ..context_mgr import ZIBEException
from .. import zbutil
import logging

@common.zibe_plugin('sam_mgr', 'Security Account Manager Plugin')
class SAMPlugin(common.ZBCommandPlugin):

    @common.command_help_string('userlist - List all system users, including machine accounts')
    def do_userlist(self, stdin, stdout, stderr, ctx, args):
        try:
            users = ctx.enum_users()
        except ZIBEException, err:
            print >> stderr, str(err)
            return

        if len(users) > 0:
            print >> stdout, ''
            print >> stdout, ' %-10s %-40s' % ('RID', 'Username')
            print >> stdout, ' ---------  -----------------------------------------'
            for u in users:
                print >> stdout, ' %-10d %-40s' % (u['rid'], u['account_name'])

            print >> stdout, ''
        else:
            print >> stderr, 'No users to enumerate'

    def help_userinfo(self):
        return '\n'.join(['userinfo <username>',
         'userinfo -r <rid>',
         '            List specific information about a user'])

    def do_userinfo(self, stdin, stdout, stderr, ctx, args):
        if len(args) != 1 and len(args) != 2:
            print >> stderr, 'Invalid syntax'
            return
        if len(args) == 2:
            if args[0] != '-r':
                print >> stderr, 'Invalid syntax'
                return
            try:
                rid = int(args[1])
            except ValueError:
                print >> stderr, 'Invalid RID'
                return

            try:
                user = ctx.get_user_info_by_rid(rid)
            except ZIBEException, err:
                print >> stderr, str(err)
                return

        else:
            try:
                user = ctx.get_user_info_by_name(args[0])
            except ZIBEException, err:
                print >> stderr, str(err)
                return

            if user:
                print >> stdout, 'User Information:'
                for k in user.keys():
                    print >> stdout, '%23s: %s' % (str(k), str(user[k]))

            print >> stderr, 'The specified user was not found'

    @common.command_help_string('useradd <username> <password> - Add an administrative user to the system')
    def do_useradd(self, stdin, stdout, stderr, ctx, args):
        if len(args) < 2:
            print >> stderr, 'Invalid syntax'
            return
        try:
            user = ctx.add_user(args[0], args[1], ctx.SAM_ADD_USER_MAKE_ADMIN)
            print >> stdout, 'Successfully added user %s' % args[0]
        except ZIBEException, err:
            print >> stderr, str(err)
            return

    def help_userdel(self):
        return '\n'.join(['userdel <username>',
         'userdel -r <rid>',
         '           Delete a user from the system'])

    def do_userdel(self, stdin, stdout, stderr, ctx, args):
        if len(args) == 0:
            print >> stderr, 'Invalid syntax'
            return
        if len(args) == 1:
            try:
                ctx.delete_user(args[0])
                print >> stdout, 'Successfully removed user %s' % args[0]
            except ZIBEException, err:
                print >> stderr, str(err)
                return

        elif len(args) == 2 and args[0] == '-r':
            rid = int(args[1])
            user = ctx.get_user_info_by_rid(rid)
            ctx.delete_user(user['UserName'])
            print >> stdout, 'Successfully removed user %d (%s)' % (rid, user['UserName'])
        else:
            print >> stderr, 'Invalid Syntax'
            return