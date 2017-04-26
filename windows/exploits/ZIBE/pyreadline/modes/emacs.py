# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\pyreadline\modes\emacs.py
# Compiled at: 2011-06-23 17:25:54
import os
import sys
import time
import pyreadline.logger as logger
from pyreadline.logger import log
from pyreadline.lineeditor.lineobj import Point
import pyreadline.lineeditor.lineobj as lineobj
import pyreadline.lineeditor.history as history
import basemode
from pyreadline.unicode_helper import ensure_unicode

def format(keyinfo):
    if len(keyinfo[-1]) != 1:
        k = keyinfo + (-1, )
    else:
        k = keyinfo + (ord(keyinfo[-1]),)
    return '(%s,%s,%s,%s,%x)' % k


in_ironpython = 'IronPython' in sys.version

class IncrementalSearchPromptMode(object):

    def __init__(self, rlobj):
        pass

    def _process_incremental_search_keyevent(self, keyinfo):
        log('_process_incremental_search_keyevent')
        keytuple = keyinfo.tuple()
        revtuples = []
        fwdtuples = []
        for ktuple, func in self.key_dispatch.iteritems():
            if func == self.reverse_search_history:
                revtuples.append(ktuple)
            elif func == self.forward_search_history:
                fwdtuples.append(ktuple)

        log('IncrementalSearchPromptMode %s %s' % (keyinfo, keytuple))
        if keyinfo.keyname == 'backspace':
            self.subsearch_query = self.subsearch_query[:-1]
            if len(self.subsearch_query) > 0:
                self.line = self.subsearch_fun(self.subsearch_query)
            else:
                self._bell()
                self.line = ''
        else:
            if keyinfo.keyname in ('return', 'escape'):
                self._bell()
                self.prompt = self.subsearch_oldprompt
                self.process_keyevent_queue = self.process_keyevent_queue[:-1]
                self._history.history_cursor = len(self._history.history)
                if keyinfo.keyname == 'escape':
                    self.l_buffer.set_line(self.subsearch_old_line)
                return True
            if keyinfo.keyname:
                pass
            elif keytuple in revtuples:
                self.subsearch_fun = self._history.reverse_search_history
                self.subsearch_prompt = "reverse-i-search%d`%s': "
                self.line = self.subsearch_fun(self.subsearch_query)
            elif keytuple in fwdtuples:
                self.subsearch_fun = self._history.forward_search_history
                self.subsearch_prompt = "forward-i-search%d`%s': "
                self.line = self.subsearch_fun(self.subsearch_query)
            elif keyinfo.control == False and keyinfo.meta == False:
                self.subsearch_query += keyinfo.char
                self.line = self.subsearch_fun(self.subsearch_query)
        self.prompt = self.subsearch_prompt % (self._history.history_cursor, self.subsearch_query)
        self.l_buffer.set_line(self.line)

    def _init_incremental_search(self, searchfun, init_event):
        log('init_incremental_search')
        self.subsearch_query = ''
        self.subsearch_fun = searchfun
        self.subsearch_old_line = self.l_buffer.get_line_text()
        queue = self.process_keyevent_queue
        queue.append(self._process_incremental_search_keyevent)
        self.subsearch_oldprompt = self.prompt
        if self.previous_func != self.reverse_search_history and self.previous_func != self.forward_search_history:
            self.subsearch_query = self.l_buffer[0:Point].get_line_text()
        if self.subsearch_fun == self.reverse_search_history:
            self.subsearch_prompt = "reverse-i-search%d`%s': "
        else:
            self.subsearch_prompt = "forward-i-search%d`%s': "
        self.prompt = self.subsearch_prompt % (self._history.history_cursor, '')
        if self.subsearch_query:
            self.line = self._process_incremental_search_keyevent(init_event)
        else:
            self.line = ''


class SearchPromptMode(object):

    def __init__(self, rlobj):
        pass

    def _process_non_incremental_search_keyevent(self, keyinfo):
        keytuple = keyinfo.tuple()
        log('SearchPromptMode %s %s' % (keyinfo, keytuple))
        history = self._history
        if keyinfo.keyname == 'backspace':
            self.non_inc_query = self.non_inc_query[:-1]
        else:
            if keyinfo.keyname in ('return', 'escape'):
                if self.non_inc_query:
                    if self.non_inc_direction == -1:
                        res = history.reverse_search_history(self.non_inc_query)
                    else:
                        res = history.forward_search_history(self.non_inc_query)
                self._bell()
                self.prompt = self.non_inc_oldprompt
                self.process_keyevent_queue = self.process_keyevent_queue[:-1]
                self._history.history_cursor = len(self._history.history)
                if keyinfo.keyname == 'escape':
                    self.l_buffer = self.non_inc_oldline
                else:
                    self.l_buffer.set_line(res)
                return False
            if keyinfo.keyname:
                pass
            elif keyinfo.control == False and keyinfo.meta == False:
                self.non_inc_query += keyinfo.char
        self.prompt = self.non_inc_oldprompt + ':' + self.non_inc_query

    def _init_non_i_search(self, direction):
        self.non_inc_direction = direction
        self.non_inc_query = ''
        self.non_inc_oldprompt = self.prompt
        self.non_inc_oldline = self.l_buffer.copy()
        self.l_buffer.reset_line()
        self.prompt = self.non_inc_oldprompt + ':'
        queue = self.process_keyevent_queue
        queue.append(self._process_non_incremental_search_keyevent)

    def non_incremental_reverse_search_history(self, e):
        return self._init_non_i_search(-1)

    def non_incremental_forward_search_history(self, e):
        return self._init_non_i_search(1)


class LeaveModeTryNext(Exception):
    pass


class DigitArgumentMode(object):

    def __init__(self, rlobj):
        pass

    def _process_digit_argument_keyevent(self, keyinfo):
        log('DigitArgumentMode.keyinfo %s' % keyinfo)
        keytuple = keyinfo.tuple()
        log('DigitArgumentMode.keytuple %s %s' % (keyinfo, keytuple))
        if keyinfo.keyname in ('return', ):
            self.prompt = self._digit_argument_oldprompt
            self.process_keyevent_queue = self.process_keyevent_queue[:-1]
            return True
        if keyinfo.keyname:
            pass
        elif keyinfo.char in '0123456789' and keyinfo.control == False and keyinfo.meta == False:
            log('arg %s %s' % (self.argument, keyinfo.char))
            self.argument = self.argument * 10 + int(keyinfo.char)
        else:
            self.prompt = self._digit_argument_oldprompt
            raise LeaveModeTryNext
        self.prompt = '(arg: %s) ' % self.argument

    def _init_digit_argument(self, keyinfo):
        c = self.console
        line = self.l_buffer.get_line_text()
        self._digit_argument_oldprompt = self.prompt
        queue = self.process_keyevent_queue
        queue = self.process_keyevent_queue
        queue.append(self._process_digit_argument_keyevent)
        if keyinfo.char == '-':
            self.argument = -1
        elif keyinfo.char in '0123456789':
            self.argument = int(keyinfo.char)
        log('<%s> %s' % (self.argument, type(self.argument)))
        self.prompt = '(arg: %s) ' % self.argument
        log('arg-init %s %s' % (self.argument, keyinfo.char))


class EmacsMode(DigitArgumentMode, IncrementalSearchPromptMode, SearchPromptMode, basemode.BaseMode):
    mode = 'emacs'

    def __init__(self, rlobj):
        basemode.BaseMode.__init__(self, rlobj)
        IncrementalSearchPromptMode.__init__(self, rlobj)
        SearchPromptMode.__init__(self, rlobj)
        DigitArgumentMode.__init__(self, rlobj)
        self._keylog = lambda x, y: None
        self.previous_func = None
        self.prompt = '>>> '
        self._insert_verbatim = False
        self.next_meta = False
        self.process_keyevent_queue = [
         self._process_keyevent]
        return

    def __repr__(self):
        return '<EmacsMode>'

    def add_key_logger(self, logfun):
        self._keylog = logfun

    def process_keyevent(self, keyinfo):
        try:
            r = self.process_keyevent_queue[-1](keyinfo)
        except LeaveModeTryNext:
            self.process_keyevent_queue = self.process_keyevent_queue[:-1]
            r = self.process_keyevent(keyinfo)

        if r:
            self.add_history(self.l_buffer.copy())
            return True
        return False

    def _process_keyevent(self, keyinfo):
        log('_process_keyevent <%s>' % keyinfo)

        def nop(e):
            pass

        if self.next_meta:
            self.next_meta = False
            keyinfo.meta = True
        keytuple = keyinfo.tuple()
        if self._insert_verbatim:
            self.insert_text(keyinfo)
            self._insert_verbatim = False
            self.argument = 0
            return False
        if keytuple in self.exit_dispatch:
            pars = (
             self.l_buffer, lineobj.EndOfLine(self.l_buffer))
            log('exit_dispatch:<%s, %s>' % pars)
            if lineobj.EndOfLine(self.l_buffer) == 0:
                raise EOFError
        if keyinfo.keyname or keyinfo.control or keyinfo.meta:
            default = nop
        else:
            default = self.self_insert
        dispatch_func = self.key_dispatch.get(keytuple, default)
        log('readline from keyboard:<%s,%s>' % (keytuple, dispatch_func))
        r = None
        if dispatch_func:
            r = dispatch_func(keyinfo)
            self._keylog(dispatch_func, self.l_buffer)
            self.l_buffer.push_undo()
        self.previous_func = dispatch_func
        return r

    def previous_history(self, e):
        self._history.previous_history(self.l_buffer)
        self.l_buffer.point = lineobj.EndOfLine
        self.finalize()

    def next_history(self, e):
        self._history.next_history(self.l_buffer)
        self.finalize()

    def beginning_of_history(self, e):
        self._history.beginning_of_history()
        self.finalize()

    def end_of_history(self, e):
        self._history.end_of_history(self.l_buffer)
        self.finalize()

    def reverse_search_history(self, e):
        log('rev_search_history')
        self._init_incremental_search(self._history.reverse_search_history, e)
        self.finalize()

    def forward_search_history(self, e):
        log('fwd_search_history')
        self._init_incremental_search(self._history.forward_search_history, e)
        self.finalize()

    def history_search_forward(self, e):
        if self.previous_func and hasattr(self._history, self.previous_func.__name__):
            self._history.lastcommand = getattr(self._history, self.previous_func.__name__)
        else:
            self._history.lastcommand = None
        q = self._history.history_search_forward(self.l_buffer)
        self.l_buffer = q
        self.l_buffer.point = q.point
        self.finalize()
        return

    def history_search_backward(self, e):
        if self.previous_func and hasattr(self._history, self.previous_func.__name__):
            self._history.lastcommand = getattr(self._history, self.previous_func.__name__)
        else:
            self._history.lastcommand = None
        q = self._history.history_search_backward(self.l_buffer)
        self.l_buffer = q
        self.l_buffer.point = q.point
        self.finalize()
        return

    def yank_nth_arg(self, e):
        self.finalize()

    def yank_last_arg(self, e):
        self.finalize()

    def forward_backward_delete_char(self, e):
        self.finalize()

    def quoted_insert(self, e):
        self._insert_verbatim = True
        self.finalize()

    def tab_insert(self, e):
        cursor = min(self.l_buffer.point, len(self.l_buffer.line_buffer))
        ws = ' ' * (self.tabstop - cursor % self.tabstop)
        self.insert_text(ws)
        self.finalize()

    def transpose_chars(self, e):
        self.l_buffer.transpose_chars()
        self.finalize()

    def transpose_words(self, e):
        self.l_buffer.transpose_words()
        self.finalize()

    def overwrite_mode(self, e):
        self.finalize()

    def kill_line(self, e):
        self.l_buffer.kill_line()
        self.finalize()

    def backward_kill_line(self, e):
        self.l_buffer.backward_kill_line()
        self.finalize()

    def unix_line_discard(self, e):
        self.l_buffer.unix_line_discard()
        self.finalize()

    def kill_whole_line(self, e):
        self.l_buffer.kill_whole_line()
        self.finalize()

    def kill_word(self, e):
        self.l_buffer.kill_word()
        self.finalize()

    forward_kill_word = kill_word

    def backward_kill_word(self, e):
        self.l_buffer.backward_kill_word()
        self.finalize()

    def unix_word_rubout(self, e):
        self.l_buffer.unix_word_rubout()
        self.finalize()

    def kill_region(self, e):
        self.finalize()

    def copy_region_as_kill(self, e):
        self.finalize()

    def copy_backward_word(self, e):
        self.finalize()

    def copy_forward_word(self, e):
        self.finalize()

    def yank(self, e):
        self.l_buffer.yank()
        self.finalize()

    def yank_pop(self, e):
        self.l_buffer.yank_pop()
        self.finalize()

    def delete_char_or_list(self, e):
        self.finalize()

    def start_kbd_macro(self, e):
        self.finalize()

    def end_kbd_macro(self, e):
        self.finalize()

    def call_last_kbd_macro(self, e):
        self.finalize()

    def re_read_init_file(self, e):
        self.finalize()

    def abort(self, e):
        self._bell()
        self.finalize()

    def do_uppercase_version(self, e):
        self.finalize()

    def prefix_meta(self, e):
        self.next_meta = True
        self.finalize()

    def undo(self, e):
        self.l_buffer.pop_undo()
        self.finalize()

    def revert_line(self, e):
        self.finalize()

    def tilde_expand(self, e):
        self.finalize()

    def set_mark(self, e):
        self.l_buffer.set_mark()
        self.finalize()

    def exchange_point_and_mark(self, e):
        self.finalize()

    def character_search(self, e):
        self.finalize()

    def character_search_backward(self, e):
        self.finalize()

    def insert_comment(self, e):
        self.finalize()

    def dump_variables(self, e):
        self.finalize()

    def dump_macros(self, e):
        self.finalize()

    def digit_argument(self, e):
        self._init_digit_argument(e)

    def universal_argument(self, e):
        pass

    def init_editing_mode(self, e):
        self._bind_exit_key('Control-d')
        self._bind_exit_key('Control-z')
        self._bind_key('space', self.self_insert)
        self._bind_key('Shift-space', self.self_insert)
        self._bind_key('Control-space', self.self_insert)
        self._bind_key('Return', self.accept_line)
        self._bind_key('Left', self.backward_char)
        self._bind_key('Control-b', self.backward_char)
        self._bind_key('Right', self.forward_char)
        self._bind_key('Control-f', self.forward_char)
        self._bind_key('Control-h', self.backward_delete_char)
        self._bind_key('BackSpace', self.backward_delete_char)
        self._bind_key('Control-BackSpace', self.backward_delete_word)
        self._bind_key('Home', self.beginning_of_line)
        self._bind_key('End', self.end_of_line)
        self._bind_key('Delete', self.delete_char)
        self._bind_key('Control-d', self.delete_char)
        self._bind_key('Clear', self.clear_screen)
        self._bind_key('Alt-f', self.forward_word)
        self._bind_key('Alt-b', self.backward_word)
        self._bind_key('Control-l', self.clear_screen)
        self._bind_key('Control-p', self.previous_history)
        self._bind_key('Up', self.history_search_backward)
        self._bind_key('Control-n', self.next_history)
        self._bind_key('Down', self.history_search_forward)
        self._bind_key('Control-a', self.beginning_of_line)
        self._bind_key('Control-e', self.end_of_line)
        self._bind_key('Alt-<', self.beginning_of_history)
        self._bind_key('Alt->', self.end_of_history)
        self._bind_key('Control-r', self.reverse_search_history)
        self._bind_key('Control-s', self.forward_search_history)
        self._bind_key('Control-Shift-r', self.forward_search_history)
        self._bind_key('Alt-p', self.non_incremental_reverse_search_history)
        self._bind_key('Alt-n', self.non_incremental_forward_search_history)
        self._bind_key('Control-z', self.undo)
        self._bind_key('Control-_', self.undo)
        self._bind_key('Escape', self.kill_whole_line)
        self._bind_key('Meta-d', self.kill_word)
        self._bind_key('Control-Delete', self.forward_delete_word)
        self._bind_key('Control-w', self.unix_word_rubout)
        self._bind_key('Control-v', self.paste)
        self._bind_key('Alt-v', self.ipython_paste)
        self._bind_key('Control-y', self.yank)
        self._bind_key('Control-k', self.kill_line)
        self._bind_key('Control-m', self.set_mark)
        self._bind_key('Control-q', self.copy_region_to_clipboard)
        self._bind_key('Control-Shift-v', self.paste_mulitline_code)
        self._bind_key('Control-Right', self.forward_word_end)
        self._bind_key('Control-Left', self.backward_word)
        self._bind_key('Shift-Right', self.forward_char_extend_selection)
        self._bind_key('Shift-Left', self.backward_char_extend_selection)
        self._bind_key('Shift-Control-Right', self.forward_word_end_extend_selection)
        self._bind_key('Shift-Control-Left', self.backward_word_extend_selection)
        self._bind_key('Shift-Home', self.beginning_of_line_extend_selection)
        self._bind_key('Shift-End', self.end_of_line_extend_selection)
        self._bind_key('numpad0', self.self_insert)
        self._bind_key('numpad1', self.self_insert)
        self._bind_key('numpad2', self.self_insert)
        self._bind_key('numpad3', self.self_insert)
        self._bind_key('numpad4', self.self_insert)
        self._bind_key('numpad5', self.self_insert)
        self._bind_key('numpad6', self.self_insert)
        self._bind_key('numpad7', self.self_insert)
        self._bind_key('numpad8', self.self_insert)
        self._bind_key('numpad9', self.self_insert)
        self._bind_key('add', self.self_insert)
        self._bind_key('subtract', self.self_insert)
        self._bind_key('multiply', self.self_insert)
        self._bind_key('divide', self.self_insert)
        self._bind_key('vk_decimal', self.self_insert)
        log('RUNNING INIT EMACS')
        for i in range(0, 10):
            self._bind_key('alt-%d' % i, self.digit_argument)

        self._bind_key('alt--', self.digit_argument)


def commonprefix(m):
    if not m:
        return ''
    prefix = m[0]
    for item in m:
        for i in range(len(prefix)):
            if prefix[:i + 1].lower() != item[:i + 1].lower():
                prefix = prefix[:i]
                if i == 0:
                    return ''
                break

    return prefix