# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\shell.py
# Compiled at: 2013-03-28 22:23:46
import cmd
import string
import binascii
from context_mgr import *
from plugin_manager import PluginManager
from zibe_errors import error_codes
import shlex
import logging
import zbutil
import time
import sys
import os
import exceptions
from Queue import Queue
import io
import re
import traceback
import inspect
from functools import wraps
from codecs import StreamWriter, StreamReader, getwriter, getreader
sys.path.append(os.path.dirname(__file__))
try:
    import readline
    HAVE_READLINE = True
except:
    HAVE_READLINE = False

class OutputWrapper(StreamWriter):

    def __init__(self, stream, errors='strict', level=logging.INFO, logger=None):
        StreamWriter.__init__(self, stream, errors=errors)
        self.loglevel = level
        if logger:
            self.logger = logger
        else:
            self.logger = logging.getLogger()

    def write(self, data):
        if data not in ('\n', '\r'):
            self.logger.log(self.loglevel, data)
        self.stream.write(data)

    def writelines(self, lines):
        for l in line:
            self.write(l)

    def reset(self):
        pass

    def seek(self, where):
        if not isinstance(self.stream, file):
            self.stream.seek(where)


class InputWrapper(StreamReader):

    def __init__(self, stream, errors='strict', level=logging.INFO, logger=None):
        StreamReader.__init__(self, stream, errors=errors)
        self.logger = logging.getLogger()
        self.loglevel = level
        if logger:
            self.logger = logger
        else:
            self.logger = logging.getLogger()

    def read(self, size=-1, chars=-1, firstline=False):
        data = self.stream.read(size)
        self.logger.log(self.loglevel, data.strip('\n'))
        return data

    def readline(self, size=-1, keepends=True):
        line = self.stream.readline(size)
        self.logger.log(self.loglevel, line.strip('\n'))
        return line

    def readlines(self, sizehint=-1, keepends=True):
        lines = self.stream.readlines(sizehint)
        for l in lines:
            self.logger.log(self.loglevel, l.strip('\n'))

        return lines

    def reset(self):
        pass


class ZIBEShell(cmd.Cmd):
    plugin_mgr = None
    prompt = 'ZIBE> '
    zb_context = None

    def __init__(self, context=None, completekey='tab', stdin=sys.stdin, stdout=sys.stdout, logger=None):
        cmd.Cmd.__init__(self, completekey, stdin, stdout)
        self.plugin_mgr = PluginManager()
        self.ctx = context
        self.use_rawinput = 1
        self.ioqueue = []
        self.stdout = OutputWrapper(stdout, logger=logger)
        self.stdin = InputWrapper(stdin, logger=logger)
        self.stderr = OutputWrapper(sys.stderr, level=logging.ERROR, logger=logger)

    def format_datetime(self, dt):
        try:
            return '%.2d/%.2d/%.4d  %.2d:%.2d' % (dt.month, dt.day, dt.year, dt.hour, dt.minute)
        except:
            return '<error calculating>'

    def emptyline(self):
        pass

    def prompt_for_input(self, prompt):
        if self.use_rawinput:
            try:
                line = raw_input(prompt)
            except EOFError:
                line = 'EOF'

        else:
            self.stdout.write(self.prompt)
            self.stdout.flush()
            self.stdin.readline()
            if not len(line):
                line = 'EOF'
            else:
                line = line.rstrip('\r\n')
        return line

    def default(self, stdin, stdout, stderr, ctx, args):
        self.stdout.write('*** Unknown syntax: %s\n' % cmd)

    def onecmd(self, line, stdin, stdout, stderr):
        cmd, args, line = self.parseline(line)
        if not line:
            return self.emptyline()
        if cmd is None:
            return self.default(stdin, stdout, stderr, self.ctx, args)
        self.lastcmd = line
        if cmd == '':
            return self.default(stdin, stdout, stderr, self.ctx, args)
        try:
            func = getattr(self, 'do_' + cmd)
        except AttributeError:
            if self.plugin_mgr.handler_exists(cmd):
                func = self.plugin_mgr.get_handler_func(cmd)
            else:
                func = self.default

        args = zbutil.parseargs(args)
        return func(stdin, stdout, stderr, self.ctx, args)
        return

    def get_compstate(self, text, arglist):
        if not text:
            return len(arglist)
        return max(len(arglist) - 1, 0)

    def complete(self, text, state):
        if state == 0:
            origline = readline.get_line_buffer()
            line = origline.lstrip()
            stripped = len(origline) - len(line)
            begidx = readline.get_begidx() - stripped
            endidx = readline.get_endidx() - stripped
            if begidx > 0:
                cmd, args, foo = self.parseline(line)
                if cmd == '':
                    compfunc = self.completedefault
                else:
                    try:
                        compfunc = getattr(self, 'complete_' + cmd)
                    except AttributeError, e:
                        compfunc = self.completedefault

            else:
                compfunc = self.completenames
            try:
                self.completion_matches = compfunc(text, origline, begidx, endidx)
            except Exception, e:
                import traceback
                logging.error('Error doing completion function: %s' % e)
                logging.error(traceback.format_exc())

        try:
            return self.completion_matches[state]
        except IndexError:
            return

        return

    def completedefault(self, *ignored):
        return []

    def getcommands(self, line):
        cmds = line.split('|')
        ret = []
        pipes = []
        if len(cmds) == 1:
            return [(cmds[0], self.stdin, self.stdout, self.stderr)]
        pipes.append(io.BytesIO())
        ret.append((cmds[0], self.stdin, OutputWrapper(pipes[0]), self.stderr))
        for i in xrange(1, len(cmds) - 1):
            pipes.append(io.ByteIO())
            ret.append((cmds[i], InputWrapper(pipes[i - 1]), OutputWrapper(pipes[i]), self.stderr))

        ret.append((cmds[-1], InputWrapper(pipes[-1]), self.stdout, self.stderr))
        return ret

    def precmd(self, cmd):
        return cmd

    def postcmd(self, stop, line):
        return stop

    def cmdloop(self, intro=None):
        self.preloop()
        if self.use_rawinput and self.completekey:
            try:
                self.old_completer = readline.get_completer()
                readline.set_completer(self.complete)
                readline.parse_and_bind(self.completekey + ': complete')
            except ImportError:
                pass

        try:
            if intro is not None:
                self.intro = intro
            if self.intro:
                print >> self.stdout, str(self.intro)
            stop = None
            while not stop:
                try:
                    if self.cmdqueue:
                        line = self.cmdqueue.pop(0)
                        self.stdout.write(self.prompt + line)
                    else:
                        if self.use_rawinput:
                            try:
                                line = raw_input(self.prompt)
                                logging.info(self.prompt)
                                logging.info('[INPUT] ' + line)
                            except EOFError:
                                line = 'EOF'

                        else:
                            self.stdout.write(self.prompt)
                            self.stdout.flush()
                            line = self.stdin.readline()
                            if not len(line):
                                line = 'EOF'
                            else:
                                line = line.rstrip('\r\n')
                        logging.log(5, line)
                        cmds = self.getcommands(line)
                        for c, stdin, stdout, stderr in cmds:
                            cmd = self.precmd(c)
                            stop = self.onecmd(cmd, stdin, stdout, stderr)
                            stop = self.postcmd(stop, line)
                            stdout.seek(0)

                except ZIBEException, e:
                    print >> stderr, 'Command exception: %s' % e
                    logging.debug(traceback.format_exc())
                except KeyboardInterrupt:
                    self.stdout.write('')
                except Exception, e:
                    print >> stderr, 'Unknown error: %s' % e
                    logging.debug(traceback.format_exc())

            self.postloop()
        finally:
            if self.use_rawinput and self.completekey:
                pass
            else:
                try:
                    readline.set_completer(self.old_completer)
                except ImportError:
                    pass

        return

    def complete_files(self, text, line, begidx, endidx):
        if self.zb_context is None:
            print >> stderr, 'No context is active'
            return []
        arglist = zbutil.parseargs(line)
        args = [arglist[0], ' '.join(arglist[1:])]
        try:
            directory = self.ctx.get_cwd()
            if len(args[1]) > 0:
                directory = os.path.join(directory, args[1])
            file_list = self.ctx.dir_list(os.path.split(directory)[0])
            return [ file['filename'] for file in file_list if file['filename'].lower().startswith(text.lower()) if not file['attributes'] & WIN32Constants.FILE_ATTRIBUTE_DIRECTORY
                   ]
        except ZIBEException, err:
            print >> stderr, 'Error in complete_files: %s' % err
            return []

        return

    def complete_directories(self, text, line, begidx, endidx):
        if self.zb_context is None:
            print >> stderr, 'No context is active'
            return []
        arglist = zbutil.parseargs(line)
        args = [arglist[0], ' '.join(arglist[1:])]
        try:
            directory = self.ctx.get_cwd()
            if len(args[1]) > 0:
                directory = os.path.join(directory, args[1])
            file_list = self.ctx.dir_list(os.path.split(directory)[0])
            return [ file['filename'] for file in file_list if file['filename'].lower().startswith(text.lower()) if file['attributes'] & WIN32Constants.FILE_ATTRIBUTE_DIRECTORY
                   ]
        except ZIBEException, err:
            print >> stderr, 'Error in complete_directories: %s' % err
            return []

        return

    def complete_regkeys(self, text, line, begidx, endidx):
        if self.zb_context is None:
            logging.warning('No context is active')
            return []
        arglist = zbutil.parseargs(line)
        args = [
         arglist[0], ' '.join(arglist[1:])]
        try:
            keys = self.ctx.enum_keys()
            return [ key for key in keys if key.lower().startswith(text.lower()) ]
        except ZIBEException, err:
            print >> stderr, str(err)
            return []

        return

    def complete_regvalues(self, text, line, begidx, endidx):
        try:
            key = self.ctx.get_cwk()
            values = self.ctx.enum_value_names()
            return [ value for value in values if value.lower().startswith(text.lower()) ]
        except ZIBEException, err:
            print >> stderr, 'Error in complete_get: %s' % err
            return []

    def help_grep(self, stdin, stdout, stderr):
        print >> stdout, "<cmd> | grep [-i] <string> - Search for a string using grep from another command's output"

    def do_grep(self, stdin, stdout, stderr, ctx, args):
        flags = 0
        if '-i' in args:
            flags = re.IGNORECASE
            args.remove('-i')
        if len(args) == 1:
            regex = re.compile(args[0], flags)
            lines = stdin.read().split('\n')
            matches = [ l for l in lines if regex.search(l) ]
            for m in matches:
                print >> stdout, m + ''

        elif len(args) == 2:
            raise NotImplementedError('Not yet implemented')

    def print_plugin_help(self, plugin_name):
        pass

    def print_topics(self, header, cmds, cmdlen, maxcol):
        if cmds:
            print >> self.stdout, '%s' % str(header)
            if self.ruler:
                print >> self.stdout, '%s' % str(self.ruler * len(header))
            self.columnize(cmds, maxcol - 1)
            print >> self.stdout, ''

    def help_help(self, stdin, stdout, stderr):
        print >> stdout, 'help [command] - Get help on a specific command, or a list of commands\n                 no arguments are specified'

    def do_help(self, stdin, stdout, stderr, ctx, args):
        if args:
            arg = args[0]
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, 'do_' + arg).__doc__
                    if doc:
                        print >> stdout, '%s' % str(doc)
                        return
                except AttributeError:
                    handler_info = self.plugin_mgr.get_handler_info(arg)
                    if handler_info and handler_info.has_key('help_func'):
                        print >> stdout, '%s' % handler_info['help_func']()
                        return

                print >> stdout, '%s' % str(self.nohelp % arg)
                return

            func(stdin, stdout, stderr)
        else:
            names = self.get_names()
            cmds_doc = []
            cmds_undoc = []
            help = {}
            for name in names:
                if name[:5] == 'help_':
                    help[name[5:]] = 1

            names.sort()
            prevname = ''
            for name in names:
                if name[:3] == 'do_':
                    if name == prevname:
                        continue
                    prevname = name
                    cmd = name[3:]
                    if cmd in help:
                        cmds_doc.append(cmd)
                        del help[cmd]
                    elif getattr(self, name).__doc__:
                        cmds_doc.append(cmd)
                    else:
                        cmds_undoc.append(cmd)

            plugins = []
            for p in self.plugin_mgr.plugins():
                plugins.append(p[0])

            print >> stdout, '%s' % str(self.doc_leader)
            self.print_topics(self.doc_header, cmds_doc, 15, 80)
            self.print_topics(self.misc_header, help.keys(), 15, 80)
            self.print_topics(self.undoc_header, cmds_undoc, 15, 80)
            for p in self.plugin_mgr.plugins():
                commands = self.plugin_mgr.plugin_commands(p[0])
                self.print_topics(p[1] + ' commands:', commands, 15, 80)

            print >> stdout, ''

    def help_plugins(self, stdin, stdout, stderr):
        print >> stdout, 'plugins - List all currently loaded plugins'

    def do_plugins(self, stdin, stdout, stderr, ctx, args):
        print >> stdout, '\nLoaded Plugins'
        print >> stdout, '----------------------------------------------------'
        for p in self.plugin_mgr.plugins():
            print >> stdout, '%-20s : %-50s' % (p[0], p[1])

        print >> stdout, ''

    def help_lpwd(self, stdin, stdout, stderr):
        print >> stdout, 'lpwd - Get the present working directory'

    def do_lpwd(self, stdin, stdout, stderr, ctx, args):
        self.do_lcd(stdin, stdout, stderr, ctx, [])

    def complete_lcd(self, text, line, begidx, endidx):
        line = line.encode('utf-8')
        args = zbutil.parseargs(line)
        try:
            dirname, fname = os.path.split(args[1])
            if dirname == '':
                dirname = self.ctx.localdir
            ret = []
            for f in os.listdir(dirname):
                relfile = os.path.relpath(os.path.join(dirname, f))
                if f.lower().startswith(fname.lower()) and os.path.isdir(relfile):
                    ret.append(f)

            return ret
        except IndexError:
            return []

    def help_lcd(self, stdin, stdout, stderr):
        print >> stdout, 'lcd <path> - Change the current working directory locally'

    def do_lcd(self, stdin, stdout, stderr, ctx, args):
        if len(args) == 0:
            print >> stdout, 'Current directory: %s' % self.ctx.localdir
        else:
            try:
                path = os.path.abspath(os.path.join(self.ctx.localdir, args[0]))
                self.ctx.lcd(path)
                print >> stdout, path
            except exceptions.EnvironmentError, e:
                logging.warning(str(e))

    def help_ldir(self, stdin, stdout, stderr):
        print >> stdout, 'ldir <relpath>- List directory contents for the current directory'

    def do_ldir(self, stdin, stdout, stderr, ctx, args):
        dircount = 0
        filecount = 0
        filesize = 0
        path = self.ctx.localdir
        if len(args) > 0:
            path = os.path.join(path, args[0])
        print >> stdout, 'Directory listing for %s' % path
        for f in sorted(os.listdir(path)):
            fqfile = os.path.join(path, f)
            os.stat_float_times(False)
            timetup = time.strptime(time.ctime(os.path.getatime(fqfile)))
            strtime = time.strftime('%y/%m/%d  %I:%M %p', timetup)
            if os.path.isdir(f):
                string = '%s    <DIR> %7s %s' % (strtime, '', f)
                print >> stdout, string
                dircount += 1
            else:
                string = '%s    %-5s %7d %s' % (strtime, '', os.path.getsize(fqfile), f)
                print >> stdout, string
                filecount += 1
                filesize += os.path.getsize(fqfile)

        print >> stdout, '                ' + '%d File(s)' % filecount + '           %d bytes' % filesize
        print >> stdout, '                ' + '%d Dir(s)' % dircount

    def complete_cd(self, text, line, begidx, endidx):
        if self.zb_context is None:
            print >> stderr, 'No context is active'
            return []
        if self.is_reghive(self.zb_context):
            return self.complete_regkeys(text, line, begidx, endidx)
        return self.complete_directories(text, line, begidx, endidx)
        return

    def help_cd(self, stdin, stdout, stderr):
        print >> stdout, 'Change the current working directory or registry key'

    def do_cd(self, stdin, stdout, stderr, ctx, args):
        if self.zb_context == None:
            print >> stderr, 'No context yet selected'
            return
        if len(args) == 0:
            print >> stdout, '%s' % self.get_current_working_path()
        elif len(args) > 1:
            print >> stderr, 'Invalid command'
        else:
            arg = zbutil.arg_to_utf8(args[0])
            try:
                if self.is_reghive(self.zb_context):
                    self.ctx.change_cwk(arg)
                else:
                    self.ctx.change_directory(arg)
            except ZIBEException, err:
                print >> stderr, str(err)
                return

            self.update_prompt()
        return

    def help_dir(self, stdin, stdout, stderr):
        print >> stdout, '\n'.join(['dir [directory][pattern] - Performs a listing of the current context. If no',
         '               directory / pattern is provides, the current working directory /',
         '               key is used. Note that pattern matching is only supported for',
         '               file shares\n'])

    def complete_dir(self, text, line, begidx, endidx):
        return self.complete_directories(text, line, begidx, endidx)

    def do_dir(self, sdtin, stdout, stderr, ctx, args):
        if self.zb_context is None:
            print >> stderr, 'No context yet selected'
        elif self.is_reghive(self.zb_context):
            try:
                keys = self.ctx.enum_keys()
                values = self.ctx.enum_values()
            except ZIBEException, err:
                print >> stderr, str(err) + ''
                return

            print >> stdout, '\n\n Registry listing for %s' % (self.zb_context + self.ctx.get_cwk())
            maxlen = max(max(map(len, keys)) if keys else 0, max(map(lambda x: len(x['name']), values)) if values else 0)
            fmt = '%%-%ds' % maxlen
            for k in keys:
                print >> stdout, fmt % k + ' <KEY>'

            maxtypelen = max(map(lambda x: len(x['type']), values)) if len(values) > 0 else 0
            fmt = '%%-%ds %%-%ds' % (maxlen, maxtypelen)
            for v in values:
                if v['type'] == 'REG_DWORD' or v['type'] == 'REG_DWORD_BIG_ENDIAN':
                    print >> stdout, fmt % (v['name'], v['type']) + '    %d' % v['data']
                else:
                    vals = zbutil.hexdump(str(v['data']), width=16).split('\n')
                    val = vals[0]
                    try:
                        val = '\n'.join([val] + map(lambda x: ' ' * (maxlen + maxtypelen + 5) + x, vals[1:]))
                    except IndexError:
                        pass

                    print >> stdout, fmt % (v['name'], v['type']) + '    %s' % val

            print >> stdout, ''
            print >> stdout, '%16d Keys(s), %14d Value(s)' % (len(keys), len(values))
        else:
            try:
                directory = None
                if len(args) > 0:
                    directory = args[0]
                file_list = self.ctx.dir_list(directory)
                print >> stdout, '\n Directory listing for %s' % self.get_current_working_path()
                folder_count = 0
                file_count = 0
                folder_size = 0
                for file in file_list:
                    folder_size += file['filesize']
                    field2 = '<DIR>         '
                    if file['attributes'] & WIN32Constants.FILE_ATTRIBUTE_DIRECTORY != WIN32Constants.FILE_ATTRIBUTE_DIRECTORY:
                        file_count += 1
                        field2 = '%14d' % file['filesize']
                    else:
                        folder_count += 1
                    if not zbutil.isprintable(file['filename']):
                        file['filename'] = binascii.hexlify(file['filename']) + ' (hexlified)'
                    print >> stdout, '%-19s  %s %s' % (self.format_datetime(file['last_access_time']), field2, file['filename'])

                print >> stdout, '%16d File(s) %-14d bytes' % (file_count, folder_size)
                print >> stdout, '%16d Dirs(s)' % folder_count
            except ZIBEException, err:
                print >> stderr, str(err)

        return

    help_ls = help_dir
    do_ls = do_dir

    def help_contexts(self, stdin, stdout, stderr):
        print >> stdout, '\n'.join(['contexts - Lists all of the available contexts. A context can either be an SMB ',
         '           share or a registry hive\n'])

    def show_contexts(self, stdin, stdout, stderr, ctx, args):
        try:
            shares = ctx.enumerate_shares()
            print >> stdout, 'Shares:'
            print >> stdout, '%-20s %-40s  %-8s' % ('Share Name', 'Remark', 'Type')
            print >> stdout, '-' * 71
            for s in shares:
                if not zbutil.isprintable(s['remark']):
                    s['remark'] = binascii.hexlify(s['remark']) + ' (hexlified)'
                print >> stdout, '%-20s %-40s  %-8x' % (s['share_name'], s['remark'], s['type'])

            print >> stdout, '\n'
            print >> stdout, 'Registry Hives:\n'
            print >> stdout, '%-30s %-30s' % ('Full Name', 'Access Name')
            print >> stdout, '------------------------------------------------------------'
            print >> stdout, '%-30s %-30s' % ('HKEY_LOCAL_MACHINE', 'HKLM')
            print >> stdout, '%-30s %-30s' % ('HKEY_CLASSES_ROOT', 'HKCR')
            print >> stdout, '%-30s %-30s' % ('HKEY_CURRENT_USER', 'HKCU')
            print >> stdout, '%-30s %-30s' % ('HKEY_USERS', 'HKU')
            print >> stdout, '%-30s %-30s' % ('HKEY_HKEY_PERFORMANCE_DATA', 'HKPD')
            print >> stdout, ''
        except ZIBEException, err:
            print >> stderr, str(err)
            if error_codes.get(err.id, ['', ''])[0] == 'NtErrorObjectNameNotFound':
                print >> stderr, "It is possible the 'browser' service is not running.  Please start the service if possible and try again"

    def do_contexts(self, stdin, stdout, stderr, ctx, args):
        self.show_contexts(stdin, stdout, stderr, ctx, args)

    def help_addshare(self, stdin, stdout, stderr):
        print >> stdout, '\n'.join(['addshare [share_name] [path] - Adds a new network share on the remote target. ',
         '           Note: share names should not contain spaces\n'])

    def do_addshare(self, stdin, stdout, stderr, ctx, args):
        if len(args) != 2:
            print >> stderr, 'Invalid command syntax. Share name and path both required'
        else:
            try:
                self.ctx.add_share(args[0], args[1])
                print >> stdout, "Successfully added '%s -> %s" % (args[0], args[1])
            except ZIBEException, err:
                print >> stderr, str(err)

    def complete_delshare(self, text, line, begidx, endidx):
        return []

    def complete_delshare(self, text, line, begidx, endidx):
        return []

    def help_delshare(self, stdin, stdout, stderr):
        print >> stdout, 'delshare [share_name] - Removes a network share from the remote target'

    def do_delshare(self, stdin, stdout, stderr, ctx, args):
        if len(args) != 1:
            print >> stderr, 'Invalid command syntax. Please only provide a share name'
        else:
            try:
                self.ctx.delete_share(args[0])
                print >> stdout, 'Successfully deleted share %s' % args[0]
            except ZIBEException, err:
                print >> stderr, str(err)

    def help_quit(self, stdin, stdout, stderr):
        print >> stdout, 'quit - Exits the shell application'

    def do_quit(self, stdin, stdout, stderr, ctx, args):
        try:
            self.ctx.finish_session()
        except ZIBEException, e:
            print >> stderr, str(e)

        return True

    def help_exit(self, stdin, stdout, stderr):
        print >> stdout, 'exit - Exits the shell application'

    def do_exit(self, stdin, stdout, stderr, ctx, args):
        return self.do_quit(stdin, stdout, stderr, ctx, args)

    def is_reghive(self, name):
        if name in ('HKCR', 'HKCU', 'HKLM', 'HKU', 'HKPD'):
            return True
        return False

    def get_current_working_path(self):
        if self.zb_context is None:
            return 'ZIBE'
        if self.is_reghive(self.zb_context):
            return self.zb_context + self.ctx.get_cwk()
        return self.zb_context + self.ctx.get_cwd()
        return

    def update_prompt(self):
        self.prompt = self.get_current_working_path() + '> '

    def help_del(self, stdin, stdout, stderr):
        print >> stdout, '\n'.join(['del <filename> - Deletes the specified file.  Wildcards are not supported \n'])

    def complete_rmdir(self, text, line, begidx, endidx):
        return []

    def help_rmdir(self, stdin, stdout, stderr):
        print >> stdout, 'rmdir [flags] <dirpath> \n                        Remove a directory and its contents (if possible).  If -f or --force\n                        are specified as flags, then do not confirm removal'

    def do_rmdir(self, stdin, stdout, stderr, ctx, args):
        if self.zb_context == None:
            logging.warning('No context selected')
            return
        if len(args) == 0:
            print >> stderr, 'The syntax of the command is incorrect'
            return
        if self.is_reghive(self.zb_context):
            try:
                self.ctx.delete_key(args[0])
            except ZIBEException, err:
                print >> stderr, str(err)
                return

        else:
            try:
                if args[0].startswith('\\'):
                    newdir = args[0]
                else:
                    curdir = self.ctx.get_cwd()
                    newdir = os.path.join(curdir, args[0])
                print >> stdout, 'Removing directory %s' % newdir
                self.ctx.remove_directory(newdir)
                print >> stdout, 'Removed!'
            except ZIBEException, err:
                print >> stderr, 'rmdir error: %s' % err
                return

        return

    def help_mkdir(self, stdin, stdout, stderr):
        print >> stdout, 'mkdir <dirname or path> - Make a new directory'

    def do_mkdir(self, stdin, stdout, stderr, ctx, args):
        if self.zb_context == None:
            logging.warning('No context selected')
            return
        if len(args) != 1:
            print >> stderr, 'The syntax of the command is incorrect'
            return
        if self.is_reghive(self.zb_context):
            try:
                self.ctx.create_key(args[0])
            except ZIBEException, err:
                print >> stderr, str(err)
                return

        else:
            try:
                if args[0].startswith('\\'):
                    newdir = args[0]
                else:
                    curdir = self.ctx.get_cwd()
                    newdir = os.path.join(curdir, args[0])
                print >> stdout, 'Creating directory %s' % newdir
                self.ctx.create_directory(newdir)
            except ZIBEException, err:
                print >> stderr, 'mkdir error: %s' % err
                return

        return

    def do_del(self, stdin, stdout, stderr, ctx, args):
        if self.zb_context == None:
            logging.warning('No context selected')
            return
        if len(args) == 0:
            print >> stderr, 'The syntax of the command is incorrect'
        if self.is_reghive(self.zb_context):
            if args[0] == '*':
                values = self.ctx.enum_value_names()
            else:
                values = args
            for v in values:
                try:
                    self.ctx.delete_value(v)
                    print >> stdout, 'Successfully deleted %s' % v
                except ZIBEException, err:
                    print >> stderr, str(err)

        if len(args) == 1 and '*' in args[0]:
            files = [ f['filename'] for f in self.ctx.dir_list(args[0]) ]
        else:
            files = args
        try:
            for f in files:
                self.ctx.delete_file(f)
                print >> stdout, "Successfully deleted '" + f + "'"

        except ZIBEException, err:
            print >> stderr, str(err)

        return

    def help_cat(self, stdin, stdout, stderr):
        print >> stdout, 'cat <filename> - Print file contents to the screen'

    def do_cat(self, stdin, stdout, stderr, ctx, args):
        if self.zb_context == None:
            logging.warning('No context selected')
            return
        if self.is_reghive(self.zb_context):
            print >> stdout, 'cat not available in this context'
            return
        if len(args) != 1:
            print >> stderr, 'Invalid syntax: cat [filename]'
            return
        try:
            file_contents = self.ctx.get_file(args[0])
            print >> stdout, file_contents
        except ZIBEException, err:
            print >> stderr, str(err)
            return

        return

    def help_use(self, stdin, stdout, stderr):
        print >> stdout, '\n'.join(['use [context_name] - Switches the current context.  For a list of contexts use ',
         "            the 'context' command\n"])

    def do_use(self, stdin, stdout, stderr, ctx, args):
        if len(args) == 1:
            reghive = args[0].upper()
            if self.is_reghive(reghive):
                self.zb_context = reghive
                self.ctx.change_hive(reghive)
            else:
                try:
                    self.ctx.use_share(args[0])
                    self.zb_context = args[0]
                except ZIBEException, err:
                    print >> stderr, str(err)

            self.update_prompt()
        elif len(args) == 0:
            self.show_contexts(stdin, stdout, stderr, ctx, args)
        else:
            print >> stderr, 'Invalid syntax'

    def help_setvalue(self, stdin, stdout, stderr):
        print >> stdout, '\n'.join(['setvalue <name> <type> <value> - Set a registry type to a ',
         '             value. Binary values can be specified as arrays, ',
         '             decimal values, or hexadecimal values\n'])

    def do_setvalue(self, stdin, stdout, stderr, ctx, args):
        if self.zb_context == None:
            logging.warning('No context selected')
            return
        if self.is_reghive(self.zb_context) is False:
            logging.warning('This command can only be used when in a registry context')
            return
        if len(args) < 3:
            print >> stderr, 'The syntax of the command is incorrect'
            return
        if args[1] == 'REG_SZ':
            value = args[2]
            type = 1
        elif args[1] == 'REG_MULTI_SZ':
            value = args[2:]
            type = 7
        elif args[1] == 'REG_BINARY':
            try:
                value = zbutil.arg2value(args[2:])
            except ValueError:
                print >> stderr, 'Unable to convert hexidecimal data to binary buffer'
                return

            type = 3
        elif args[1] == 'REG_DWORD':
            try:
                value = zbutil.arg2value(args[2], size=4)
            except ValueError:
                print >> stderr, 'Invalid integer value'
                return

            type = 4
        else:
            print >> stderr, 'Unsupported data type.  Only REG_SZ, REG_MULTI_SZ, REG_DWORD, and REG_BINARY supported'
            return
        try:
            logging.debug('set %s %s %s' % (args[0], type, value))
            self.ctx.set_reg_value(args[0], type, value)
        except ZIBEException, err:
            print >> stderr, str(err)

        return

    def help_put(self, stdin, stdout, stderr):
        print >> stdout, '\n'.join(['put <local_filename> <remote_filename> - Uploads a file to the remote ',
         '            target.  This command only works in the SMB / file context. If',
         '            you want to set a registry value, use the setvalue command\n'])

    def complete_put(self, text, line, begidx, endidx):
        return []

    def do_put(self, stdin, stdout, stderr, ctx, args):
        if self.zb_context == None:
            logging.warning('No context selected')
            return
        if len(args) != 2:
            print >> stderr, 'The syntax of the command is incorrect'
            return
        try:
            with open(args[0], 'rb') as fp:
                file = fp.read()
        except IOError, err:
            print >> stderr, 'Failed to open local file: %s' % str(err)
            return

        try:
            self.ctx.put_file(args[1], file)
            print >> stdout, 'Successfully put 1 file'
        except ZIBEException, err:
            print >> stderr, str(err)

        return

    def _print_regvalue(self, stdin, stdout, stderr, data):
        print >> stdout, '    Name: %-20s Type: %-15s' % (data[0], data[1])
        if data[1] == 'REG_SZ' or data[1] == 'REG_EXPAND_SZ':
            print >> stdout, "        '%s'" % data[2]
        elif data[1] == 'REG_DWORD' or data[1] == 'REG_QWORD':
            print >> stdout, '        0x%.8x (%d)' % (data[2], data[2])
        elif data[1] == 'REG_MULTI_SZ':
            for s in data[2]:
                print >> stdout, "        '%s'" % s

        else:
            if data[1] == 'REG_BINARY':
                i = 1
                hex_rep = ''
                string_rep = ''
                for c in data[2]:
                    hex_rep += '%.2x ' % ord(c)
                    if c in string.printable:
                        string_rep += c
                    else:
                        string_rep += '.'
                    if i % 16 == 0:
                        print >> stdout, '        ' + hex_rep + ' ' + string_rep
                        hex_rep = ''
                        string_rep = ''
                    i += 1

                if hex_rep != '':
                    print >> stdout, '        %-48s %s' % (hex_rep, string_rep)
            print >> stderr, 'Unexpected data type'

    def help_get(self, stdin, stdout, stderr):
        print >> stdout, '\n'.join(['get - retrieves a file or registry value. This command functions ',
         '            differently based on the current context.  When a registry key',
         '            is selected, use the following syntax:\n',
         '            get <value_name|*> Prints the specified registry value to the',
         "                       console.  The '*' character prints all values in",
         '                       the current context.',
         '            get <remote_filename> [local_filename] - Downloads a file from ',
         '                       the remote  target, writing the result to the ',
         '                       specified path.  This will overwrite any existing file\n'])

    def complete_get(self, text, line, begidx, endidx):
        if self.is_reghive(self.zb_context):
            return self.complete_regvalues(text, line, begidx, endidx)
        return []

    def do_get(self, stdin, stdout, stderr, ctx, args):
        if self.zb_context == None:
            print >> stderr, 'No context selected'
            return
        if self.is_reghive(self.zb_context):
            if len(args) != 1:
                print >> stderr, 'The syntax of the command is incorrect'
            else:
                try:
                    result = self.ctx.get_reg_values(args[0])
                    for r in result:
                        self._print_regvalue(stdin, stdout, stderr, r)

                except ZIBEException, err:
                    print >> stderr, str(err)
                    return

        else:
            dst = None
            src = None
            if len(args) < 1 or len(args) > 2:
                print >> stderr, 'You must provide a remote name at a minimum'
            elif len(args) == 1:
                dst = args[0]
                filename = os.path.split(dst)[1]
                src = os.path.join(self.ctx.localdir, filename)
            elif len(args) == 2:
                dst = args[0]
                src = args[1]
            try:
                file_contents = self.ctx.get_file(dst)
                with open(src, 'wb') as fh:
                    fh.write(file_contents)
                print >> stdout, '(%d bytes) [remote]%s -> [local]%s' % (len(file_contents), dst, src)
            except ZIBEException, err:
                print >> stdout, 'Failed! %s' % str(err)
                print >> stderr, str(err)
                return

        return

    def complete_info(self, text, line, begidx, endidx):
        return self.complete_files(text, line, begidx, endidx)

    def help_info(self, stdin, stdout, stderr):
        print >> stdout, '\n'.join(['info <filename> - Retrieves information about the specified filename. Note that ',
         '            this command only works in the SMB file context\n'])

    def do_info(self, stdin, stdout, stderr, ctx, args):
        if self.zb_context == None:
            print >> stderr, 'No context selected'
            return
        if len(args) == 1:
            if self.is_reghive(self.zb_context):
                print >> stderr, 'Command not supported in this context'
                return
            try:
                fi = self.ctx.get_file_details(args[0])
            except ZIBEException, err:
                print >> stderr, str(err)
                return

            print >> stdout, 'Information for file %s' % fi['filename']
            print >> stdout, '   Creation Time: %s' % self.format_datetime(fi['creation_time'])
            print >> stdout, '       File Size: %s' % str(fi['filesize'])
            print >> stdout, '     Last Access: %s' % self.format_datetime(fi['last_access_time'])
            print >> stdout, '      Last Write: %s' % self.format_datetime(fi['last_write_time'])
            print >> stdout, '      Attributes: 0x%x' % fi['attributes']
            if fi['attributes'] & WIN32Constants.FILE_ATTRIBUTE_READONLY:
                print >> stdout, '      FILE_ATTRIBUTE_READONLY'
            if fi['attributes'] & WIN32Constants.FILE_ATTRIBUTE_HIDDEN:
                print >> stdout, '      FILE_ATTRIBUTE_HIDDEN'
            if fi['attributes'] & WIN32Constants.FILE_ATTRIBUTE_SYSTEM:
                print >> stdout, '      FILE_ATTRIBUTE_SYSTEM'
            if fi['attributes'] & WIN32Constants.FILE_ATTRIBUTE_DIRECTORY:
                print >> stdout, '      FILE_ATTRIBUTE_DIRECTORY'
            if fi['attributes'] & WIN32Constants.FILE_ATTRIBUTE_ARCHIVE:
                print >> stdout, '      FILE_ATTRIBUTE_ARCHIVE'
            if fi['attributes'] & WIN32Constants.FILE_ATTRIBUTE_NORMAL:
                print >> stdout, '      FILE_ATTRIBUTE_NORMAL'
            if fi['attributes'] & WIN32Constants.FILE_ATTRIBUTE_TEMPORARY:
                print >> stdout, '      FILE_ATTRIBUTE_TEMPORARY'
            if fi['attributes'] & WIN32Constants.FILE_ATTRIBUTE_COMPRESSED:
                print >> stdout, '      FILE_ATTRIBUTE_COMPRESSED'
            if fi['attributes'] & WIN32Constants.FILE_ATTRIBUTE_ENCRYPTED:
                print >> stdout, '      FILE_ATTRIBUTE_ENCRYPTED'
            print >> stdout, ''
        else:
            print >> stderr, 'Error: No file specified'
        return

    def help_versionstrings(self, stdin, stdout, stderr):
        print >> stdout, 'Get remotely reported version strings'

    def do_versionstrings(self, stdin, stdout, stderr, ctx, args):
        osStr, lmStr = ctx.get_version_strings()
        print >> stdout, 'OS String: %s' % osStr
        print >> stdout, 'LM String: %s' % lmStr