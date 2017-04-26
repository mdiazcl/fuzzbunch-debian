# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\plugins\service_control_manager.py
# Compiled at: 2013-02-27 18:02:46
from . import common
from ..context_mgr import ZIBEException
from .. import zbutil
import logging

@common.zibe_plugin('scm_plugin', 'Service Control Manager')
class ServiceControlManagerPlugin(common.ZBCommandPlugin):

    @common.command_help_string('servicelist - List all services on the box and their statuses')
    def do_servicelist(self, stdin, stdout, stderr, ctx, args):
        try:
            show_drivers = True
            show_svcs = True
            if len(args) > 0:
                filter = args[0].lower()
                if filter == 'driver' or filter == 'd':
                    show_svcs = False
                elif filter == 'service' or filter == 'svc' or filter == 's':
                    show_drivers = False
            svc_data = ctx.get_services()
            print >> stdout, 'Services:'
            print >> stdout, '%-15s %-4s %-35s %-13s %-7s' % ('Name', 'PID', 'Display Name',
                                                              'Type', 'State')
            print >> stdout, '--------------------------------------------------------------------------------'
            for s in svc_data:
                if show_svcs is True and s['type'].startswith('Service') or show_drivers is True and s['type'].startswith('Driver'):
                    print >> stdout, '%-15s %-4d %-35s  %-13s %-7s' % (s['service_name'][:15], s['pid'], s['display_name'][:35], s['type'], s['state'])

            print >> stdout, ''
        except ZIBEException, err:
            print >> stderr, str(err)
            return

    @common.command_help_string('servicestart <service> - Start a service')
    def do_servicestart(self, stdin, stdout, stderr, ctx, args):
        if len(args) == 0:
            print >> stderr, 'You must provide a service name\n'
            return
        try:
            ctx.start_service(args[0])
        except ZIBEException, err:
            print >> stderr, 'Failed to start service %s!\n' % args[0]
            if err.id == 1058:
                print >> stderr, 'The service is disabled and cannot be started\n'
            else:
                print >> stderr, str(err)
            return

    @common.command_help_string('servicestop <service> - Stop a service')
    def do_servicestop(self, stdin, stdout, stderr, ctx, args):
        if len(args) == 0:
            print >> stderr, 'Must provide a service name\n'
            return
        try:
            ctx.stop_service(args[0])
        except ZIBEException, err:
            print >> stderr, str(err)
            return

    @common.command_help_string('serviceinfo <service> - Retrieve information about a service')
    def do_serviceinfo(self, stdin, stdout, stderr, ctx, args):
        if len(args) == 0:
            print >> stderr, 'Must provide a service name'
            return
        try:
            config = ctx.query_service_config(args[0])
        except ZIBEException, err:
            print >> stderr, str(err)
            return

        print >> stdout, '** Service Configuration:'
        print >> stdout, '          Name: %s' % args[0]
        print >> stdout, '  Display Name: %s' % config['display_name']
        print >> stdout, '          Path: %s' % config['binarypath_name']
        print >> stdout, '          Type: %s' % config['type']
        print >> stdout, '    Start Type: %s' % config['start_type']
        print >> stdout, '  Dependencies: %s' % config['dependencies']
        print >> stdout, '    Load Group: %s' % config['load_order_group']
        try:
            status = ctx.query_service_status(args[0])
        except ZIBEException, err:
            print >> stderr, str(err)
            return

        print >> stdout, '     Exit Code: %s' % status['svc_exit_code']
        print >> stdout, '         State: %s' % status['state']
        print >> stdout, '           PID: %d' % status['pid']