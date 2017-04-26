# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\pyreadline\modes\notemacs.py
# Compiled at: 2011-06-23 17:25:54
import os
import pyreadline.logger as logger
from pyreadline.logger import log
import pyreadline.lineeditor.lineobj as lineobj
import pyreadline.lineeditor.history as history
import basemode

class NotEmacsMode(basemode.BaseMode):
    mode = 'notemacs'

    def __init__(self, rlobj):
        super(NotEmacsMode, self).__init__(rlobj)

    def __repr__(self):
        return '<NotEmacsMode>'

    def _readline_from_keyboard(self):
        c = self.console
        while 1:
            self._update_line()
            event = c.getkeypress()
            if self.next_meta:
                self.next_meta = False
                control, meta, shift, code = event.keyinfo
                event.keyinfo = (control, True, shift, code)
            if event.keyinfo in self.exit_dispatch:
                if lineobj.EndOfLine(self.l_buffer) == 0:
                    raise EOFError
            dispatch_func = self.key_dispatch.get(event.keyinfo, self.self_insert)
            log('readline from keyboard:%s' % (event.keyinfo,))
            r = None
            if dispatch_func:
                r = dispatch_func(event)
                self.l_buffer.push_undo()
            self.previous_func = dispatch_func
            if r:
                self._update_line()
                break

        return

    def readline(self, prompt=''):
        if self.first_prompt:
            self.first_prompt = False
            if self.startup_hook:
                try:
                    self.startup_hook()
                except:
                    print 'startup hook failed'
                    traceback.print_exc()

        c = self.console
        self.l_buffer.reset_line()
        self.prompt = prompt
        self._print_prompt()
        if self.pre_input_hook:
            try:
                self.pre_input_hook()
            except:
                print 'pre_input_hook failed'
                traceback.print_exc()
                self.pre_input_hook = None

        log('in readline: %s' % self.paste_line_buffer)
        if len(self.paste_line_buffer) > 0:
            self.l_buffer = lineobj.ReadlineTextBuffer(self.paste_line_buffer[0])
            self._update_line()
            self.paste_line_buffer = self.paste_line_buffer[1:]
            c.write('\r\n')
        else:
            self._readline_from_keyboard()
            c.write('\r\n')
        self.add_history(self.l_buffer.copy())
        log('returning(%s)' % self.l_buffer.get_line_text())
        return self.l_buffer.get_line_text() + '\n'

    def beginning_of_line(self, e):
        self.l_buffer.beginning_of_line()

    def end_of_line(self, e):
        self.l_buffer.end_of_line()

    def forward_char(self, e):
        self.l_buffer.forward_char()

    def backward_char(self, e):
        self.l_buffer.backward_char()

    def forward_word(self, e):
        self.l_buffer.forward_word()

    def backward_word(self, e):
        self.l_buffer.backward_word()

    def clear_screen(self, e):
        self.console.page()

    def redraw_current_line(self, e):
        pass

    def accept_line(self, e):
        return True

    def previous_history(self, e):
        self._history.previous_history(self.l_buffer)

    def next_history(self, e):
        self._history.next_history(self.l_buffer)

    def beginning_of_history(self, e):
        self._history.beginning_of_history()

    def end_of_history(self, e):
        self._history.end_of_history(self.l_buffer)

    def _i_search(self, searchfun, direction, init_event):
        c = self.console
        line = self.get_line_buffer()
        query = ''
        hc_start = self._history.history_cursor
        while 1:
            x, y = self.prompt_end_pos
            c.pos(0, y)
            if direction < 0:
                prompt = 'reverse-i-search'
            else:
                prompt = 'forward-i-search'
            scroll = c.write_scrolling("%s`%s': %s" % (prompt, query, line))
            self._update_prompt_pos(scroll)
            self._clear_after()
            event = c.getkeypress()
            if event.keysym == 'BackSpace':
                if len(query) > 0:
                    query = query[:-1]
                    self._history.history_cursor = hc_start
                else:
                    self._bell()
            elif event.char in string.letters + string.digits + string.punctuation + ' ':
                self._history.history_cursor = hc_start
                query += event.char
            elif event.keyinfo == init_event.keyinfo:
                self._history.history_cursor += direction
                line = searchfun(query)
            else:
                if event.keysym != 'Return':
                    self._bell()
                break
            line = searchfun(query)

        px, py = self.prompt_begin_pos
        c.pos(0, py)
        self.l_buffer.set_line(line)
        self._print_prompt()
        self._history.history_cursor = len(self._history.history)

    def reverse_search_history(self, e):
        self._i_search(self._history.reverse_search_history, -1, e)

    def forward_search_history(self, e):
        self._i_search(self._history.forward_search_history, 1, e)

    def non_incremental_reverse_search_history(self, e):
        self._history.non_incremental_reverse_search_history(self.l_buffer)

    def non_incremental_forward_search_history(self, e):
        self._history.non_incremental_reverse_search_history(self.l_buffer)

    def history_search_forward(self, e):
        self.l_buffer = self._history.history_search_forward(self.l_buffer)

    def history_search_backward(self, e):
        self.l_buffer = self._history.history_search_backward(self.l_buffer)

    def yank_nth_arg(self, e):
        pass

    def yank_last_arg(self, e):
        pass

    def delete_char(self, e):
        self.l_buffer.delete_char()

    def backward_delete_char(self, e):
        self.l_buffer.backward_delete_char()

    def forward_backward_delete_char(self, e):
        pass

    def quoted_insert(self, e):
        e = self.console.getkeypress()
        self.insert_text(e.char)

    def tab_insert(self, e):
        cursor = min(self.l_buffer.point, len(self.l_buffer.line_buffer))
        ws = ' ' * (self.tabstop - cursor % self.tabstop)
        self.insert_text(ws)

    def self_insert(self, e):
        if ord(e.char) != 0:
            self.insert_text(e.char)

    def transpose_chars(self, e):
        self.l_buffer.transpose_chars()

    def transpose_words(self, e):
        self.l_buffer.transpose_words()

    def upcase_word(self, e):
        self.l_buffer.upcase_word()

    def downcase_word(self, e):
        self.l_buffer.downcase_word()

    def capitalize_word(self, e):
        self.l_buffer.capitalize_word()

    def overwrite_mode(self, e):
        pass

    def kill_line(self, e):
        self.l_buffer.kill_line()

    def backward_kill_line(self, e):
        self.l_buffer.backward_kill_line()

    def unix_line_discard(self, e):
        self.l_buffer.unix_line_discard()

    def kill_whole_line(self, e):
        self.l_buffer.kill_whole_line()

    def kill_word(self, e):
        self.l_buffer.kill_word()

    def backward_kill_word(self, e):
        self.l_buffer.backward_kill_word()

    def unix_word_rubout(self, e):
        self.l_buffer.unix_word_rubout()

    def delete_horizontal_space(self, e):
        pass

    def kill_region(self, e):
        pass

    def copy_region_as_kill(self, e):
        pass

    def copy_region_to_clipboard(self, e):
        if self.enable_win32_clipboard:
            mark = min(self.l_buffer.mark, len(self.l_buffer.line_buffer))
            cursor = min(self.l_buffer.point, len(self.l_buffer.line_buffer))
            if self.l_buffer.mark == -1:
                return
            begin = min(cursor, mark)
            end = max(cursor, mark)
            toclipboard = ''.join(self.l_buffer.line_buffer[begin:end])
            clipboard.SetClipboardText(str(toclipboard))

    def copy_backward_word(self, e):
        pass

    def copy_forward_word(self, e):
        pass

    def paste(self, e):
        if self.enable_win32_clipboard:
            txt = clipboard.get_clipboard_text_and_convert(False)
            self.insert_text(txt)

    def paste_mulitline_code(self, e):
        reg = re.compile('\r?\n')
        if self.enable_win32_clipboard:
            txt = clipboard.get_clipboard_text_and_convert(False)
            t = reg.split(txt)
            t = [ row for row in t if row.strip() != '' ]
            if t != ['']:
                self.insert_text(t[0])
                self.add_history(self.l_buffer.copy())
                self.paste_line_buffer = t[1:]
                log('multi: %s' % self.paste_line_buffer)
                return True
            return False

    def ipython_paste(self, e):
        if self.enable_win32_clipboard:
            txt = clipboard.get_clipboard_text_and_convert(self.enable_ipython_paste_list_of_lists)
            if self.enable_ipython_paste_for_paths:
                if len(txt) < 300 and '\t' not in txt and '\n' not in txt:
                    txt = txt.replace('\\', '/').replace(' ', '\\ ')
            self.insert_text(txt)

    def yank(self, e):
        pass

    def yank_pop(self, e):
        pass

    def digit_argument(self, e):
        pass

    def universal_argument(self, e):
        pass

    def delete_char_or_list(self, e):
        pass

    def start_kbd_macro(self, e):
        pass

    def end_kbd_macro(self, e):
        pass

    def call_last_kbd_macro(self, e):
        pass

    def re_read_init_file(self, e):
        pass

    def abort(self, e):
        self._bell()

    def do_uppercase_version(self, e):
        pass

    def prefix_meta(self, e):
        self.next_meta = True

    def undo(self, e):
        self.l_buffer.pop_undo()

    def revert_line(self, e):
        pass

    def tilde_expand(self, e):
        pass

    def set_mark(self, e):
        self.l_buffer.set_mark()

    def exchange_point_and_mark(self, e):
        pass

    def character_search(self, e):
        pass

    def character_search_backward(self, e):
        pass

    def insert_comment(self, e):
        pass

    def dump_functions(self, e):
        pass

    def dump_variables(self, e):
        pass

    def dump_macros(self, e):
        pass

    def init_editing_mode(self, e):
        self._bind_exit_key('Control-d')
        self._bind_exit_key('Control-z')
        self._bind_key('Shift-space', self.self_insert)
        self._bind_key('Control-space', self.self_insert)
        self._bind_key('Return', self.accept_line)
        self._bind_key('Left', self.backward_char)
        self._bind_key('Control-b', self.backward_char)
        self._bind_key('Right', self.forward_char)
        self._bind_key('Control-f', self.forward_char)
        self._bind_key('BackSpace', self.backward_delete_char)
        self._bind_key('Home', self.beginning_of_line)
        self._bind_key('End', self.end_of_line)
        self._bind_key('Delete', self.delete_char)
        self._bind_key('Control-d', self.delete_char)
        self._bind_key('Clear', self.clear_screen)


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