# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\plugins\job_manager.py
# Compiled at: 2013-02-27 18:02:46
from . import common
from ..context_mgr import ZIBEException
from .. import zbutil
import logging

@common.zibe_plugin('job_mgr', 'Task Scheduler Plugin')
class TaskSchedulerPlugin(common.ZBCommandPlugin):

    @common.command_help_string('joblist - List scheduled jobs')
    def do_joblist(self, stdin, stdout, stderr, ctx, args):
        try:
            jobs = ctx.enumerate_jobs()
        except ZIBEException, err:
            print >> stderr, str(err)
            return

        if len(jobs) > 0:
            print >> stdout, '%-10s %-40s %-17s %-9s' % ('ID', 'Command', 'Time', 'Flags')
            print >> stdout, '---------- ---------------------------------------- ----------------- ---------'
            for j in jobs:
                print >> stdout, '%-10d %-40s %-17s %-9x' % (j['job_id'], j['cmd'], j['job_time'], j['flags'])

            print >> stdout, ''
        else:
            print >> stdout, 'No Jobs currently scheduled'

    @common.command_help_string('jobdel <jobid> - Delete a scheduled job')
    def do_jobdel(self, stdin, stdout, stderr, ctx, args):
        if len(args) != 1:
            print >> stderr, 'No job ID provided'
            return
        try:
            job_id = int(args[0])
        except TypeError:
            print >> stderr, 'Invalid job id'
            return

        try:
            ctx.delete_job(job_id)
        except ZIBEException, err:
            print >> stderr, str(err)
            return

        print >> stdout, 'Successfully deleted job %d' % job_id

    def help_jobadd(self):
        return '\n'.join(['jobadd <command> <time|now> - Schedules a new job to be run by the remote AT service',
         '       command - a fully qualified command with options.',
         "       time - The time which the command should be run.  the 'now' convenience will",
         '              schedule the next available time slot'])

    def do_jobadd(self, stdin, stdout, stderr, ctx, args):
        if len(args) != 2:
            print >> stderr, 'Invalid Syntax'
            return
        try:
            if args[1].lower() == 'now':
                job_id = ctx.add_job_now(args[0])
            else:
                times = args[1].split(':')
                if len(times) != 2:
                    print >> stderr, 'Invalid time'
                    return
                try:
                    hours = int(times[0])
                    mins = int(times[1])
                except TypeError:
                    print >> stderr, 'Invalid time'
                    return

                job_id = ctx.add_job(args[0], hours, mins)
        except ZIBEException, err:
            print >> stdout, str(err)
            return

        print >> stdout, 'Successfully added job.  Job ID is %d' % job_id