# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\plugins\tunnel_manager.py
# Compiled at: 2013-02-27 18:02:46
from . import common
from ..context_mgr import ZIBEException
from .. import zbutil
import logging

@common.zibe_plugin('tunnel_manager', 'TCP Tunnel Manager')
class TunnelManagerPlugin(common.ZBCommandPlugin):

    @common.command_help_string('tunneladd [connect_ip] [connect_port] [listen_port] - Sets up a remote tunnel. Note that IPv6 must be enabled')
    def do_tunneladd(self, stdin, stdout, stderr, ctx, args):
        if len(args) != 3:
            print >> stderr, 'Not enough parameters'
            return
        try:
            connect_port = int(args[1])
            listen_port = int(args[2])
        except ValueError:
            print >> stderr, 'Invalid port'
            return

        if connect_port > 65535 or listen_port > 65535:
            print >> stderr, 'Invalid port'
            return
        try:
            ctx.add_tunnel(args[0], connect_port, listen_port)
        except ZIBEException, err:
            print >> stderr, str(err)
            return

        print >> stdout, 'Tunnel successfully created'

    @common.command_help_string('tunneldel [listen_port] - Deletes an existing tunnel on the remote machine')
    def do_tunneldel(self, stdin, stdout, stderr, ctx, args):
        if len(args) != 1:
            print >> stderr, 'Invalid listen port'
            return
        try:
            listen_port = int(args[0])
        except ValueError:
            print >> stderr, 'Invalid listen port'
            return

        try:
            ctx.delete_tunnel(listen_port)
        except ZIBEException, err:
            print >> stderr, str(err)
            return

        print >> stdout, 'Tunnel successfully deleted'

    @common.command_help_string('tunnellist - Lists all existing TCP tunnels')
    def do_tunnellist(self, stdin, stdout, stderr, ctx, args):
        try:
            tunnels = ctx.enum_tunnels()
        except ZIBEException, err:
            print >> stderr, str(err)
            return

        tunnel_types = [
         '4to4', '4to6', '6to4', '6to6']
        if len(tunnels) > 0:
            print >> stdout, '%-5s %-20s %-13s %-13s' % ('Type', 'Connect IP Address',
                                                         'Connect Port', 'Listen Port')
            print >> stdout, '------------------------------------------------------'
            for t in tunnels:
                print >> stdout, '%-5s %-20s %-13s %-13s' % (tunnel_types[t['tunnel_type']], t['connect_ip_address'], t['connect_port'], t['listen_port'])

            print >> stdout, ''
        else:
            print >> stderr, 'No tunnels currently running'