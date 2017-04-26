# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\pyreadline\modes\basemode.py
# Compiled at: 2011-06-23 17:25:54
import os
import re
import math
import glob
import sys
import time
import pyreadline.logger as logger
from pyreadline.logger import log
from pyreadline.keysyms.common import make_KeyPress_from_keydescr
import pyreadline.lineeditor.lineobj as lineobj
import pyreadline.lineeditor.history as history
import pyreadline.clipboard as clipboard
from pyreadline.error import ReadlineError, GetSetError
from pyreadline.unicode_helper import ensure_str, ensure_unicode
in_ironpython = 'IronPython' in sys.version

class BaseMode(object):
    mode = 'base'

    def __init__(self, rlobj):
        self.argument = 0
        self.rlobj = rlobj
        self.exit_dispatch = {}
        self.key_dispatch = {}
        self.argument = 1
        self.prevargument = None
        self.l_buffer = lineobj.ReadLineTextBuffer('')
        self._history = history.LineHistory()
        self.completer_delims = ' \t\n"\\\'`@$><=;|&{('
        self.show_all_if_ambiguous = 'off'
        self.mark_directories = 'on'
        self.complete_filesystem = 'off'
        self.completer = None
        self.begidx = 0
        self.endidx = 0
        self.tabstop = 4
        self.startup_hook = None
        self.pre_input_hook = None
        self.first_prompt = True
        self.cursor_size = 25
        self.prompt = '>>> '
        self.enable_ipython_paste_for_paths = True
        self.enable_ipython_paste_list_of_lists = True
        self.enable_win32_clipboard = True
        self.paste_line_buffer = []
        self._sub_modes = []
        return

    def __repr__(self):
        return '<BaseMode>'

    def _gs(x):

        def g(self):
            return getattr(self.rlobj, x)

        def s(self, q):
            setattr(self.rlobj, x, q)

        return (
         g, s)

    def _g(x):

        def g(self):
            return getattr(self.rlobj, x)

        return g

    def _argreset(self):
        val = self.argument
        self.argument = 0
        if val == 0:
            val = 1
        return val

    argument_reset = property(_argreset)
    ctrl_c_tap_time_interval = property(*_gs('ctrl_c_tap_time_interval'))
    allow_ctrl_c = property(*_gs('allow_ctrl_c'))
    _print_prompt = property(_g('_print_prompt'))
    _update_line = property(_g('_update_line'))
    console = property(_g('console'))
    prompt_begin_pos = property(_g('prompt_begin_pos'))
    prompt_end_pos = property(_g('prompt_end_pos'))
    _bell = property(_g('_bell'))
    bell_style = property(_g('bell_style'))
    _clear_after = property(_g('_clear_after'))
    _update_prompt_pos = property(_g('_update_prompt_pos'))

    def process_keyevent(self, keyinfo):
        raise NotImplementedError

    def readline_setup(self, prompt=''):
        self.l_buffer.selection_mark = -1
        if self.first_prompt:
            self.first_prompt = False
            if self.startup_hook:
                try:
                    self.startup_hook()
                except:
                    print 'startup hook failed'
                    traceback.print_exc()

        self.l_buffer.reset_line()
        self.prompt = prompt
        if self.pre_input_hook:
            try:
                self.pre_input_hook()
            except:
                print 'pre_input_hook failed'
                traceback.print_exc()
                self.pre_input_hook = None

        return

    def finalize(self):
        self.argument = 0

    def add_history(self, text):
        self._history.add_history(lineobj.ReadLineTextBuffer(text))

    def rl_settings_to_string(self):
        out = [
         '%-20s: %s' % ('show all if ambigous', self.show_all_if_ambiguous)]
        out.append('%-20s: %s' % ('mark_directories', self.mark_directories))
        out.append('%-20s: %s' % ('bell_style', self.bell_style))
        out.append('------------- key bindings ------------')
        tablepat = '%-7s %-7s %-7s %-15s %-15s '
        out.append(tablepat % ('Control', 'Meta', 'Shift', 'Keycode/char', 'Function'))
        bindings = [ (k[0], k[1], k[2], k[3], v.__name__) for k, v in self.key_dispatch.iteritems() ]
        bindings.sort()
        for key in bindings:
            out.append(tablepat % key)

        return out

    def _bind_key(self, key, func):
        if not callable(func):
            print 'Trying to bind non method to keystroke:%s,%s' % (key, func)
            raise ReadlineError('Trying to bind non method to keystroke:%s,%s,%s,%s' % (key, func, type(func), type(self._bind_key)))
        keyinfo = make_KeyPress_from_keydescr(key.lower()).tuple()
        log('>>>%s -> %s<<<' % (keyinfo, func.__name__))
        self.key_dispatch[keyinfo] = func

    def _bind_exit_key(self, key):
        keyinfo = make_KeyPress_from_keydescr(key.lower()).tuple()
        self.exit_dispatch[keyinfo] = None
        return

    def init_editing_mode(self, e):
        raise NotImplementedError

    def _get_completions--- This code section failed: ---

 182       0  BUILD_LIST_0          0 
           3  STORE_FAST            1  'completions'

 183       6  LOAD_FAST             0  'self'
           9  LOAD_ATTR             0  'l_buffer'
          12  LOAD_ATTR             1  'point'
          15  LOAD_FAST             0  'self'
          18  STORE_ATTR            2  'begidx'

 184      21  LOAD_FAST             0  'self'
          24  LOAD_ATTR             0  'l_buffer'
          27  LOAD_ATTR             1  'point'
          30  LOAD_FAST             0  'self'
          33  STORE_ATTR            3  'endidx'

 185      36  LOAD_FAST             0  'self'
          39  LOAD_ATTR             0  'l_buffer'
          42  LOAD_ATTR             4  'line_buffer'
          45  STORE_FAST            2  'buf'

 186      48  LOAD_FAST             0  'self'
          51  LOAD_ATTR             5  'completer'
          54  JUMP_IF_FALSE       291  'to 348'
          57  POP_TOP          

 188      58  SETUP_LOOP           79  'to 140'
          61  LOAD_FAST             0  'self'
          64  LOAD_ATTR             2  'begidx'
          67  LOAD_CONST            1  ''
          70  COMPARE_OP            4  '>'
          73  JUMP_IF_FALSE        62  'to 138'
          76  POP_TOP          

 189      77  LOAD_FAST             0  'self'
          80  DUP_TOP          
          81  LOAD_ATTR             2  'begidx'
          84  LOAD_CONST            2  1
          87  INPLACE_SUBTRACT 
          88  ROT_TWO          
          89  STORE_ATTR            2  'begidx'

 190      92  LOAD_FAST             2  'buf'
          95  LOAD_FAST             0  'self'
          98  LOAD_ATTR             2  'begidx'
         101  BINARY_SUBSCR    
         102  LOAD_FAST             0  'self'
         105  LOAD_ATTR             6  'completer_delims'
         108  COMPARE_OP            6  'in'
         111  JUMP_IF_FALSE        20  'to 134'
         114  POP_TOP          

 191     115  LOAD_FAST             0  'self'
         118  DUP_TOP          
         119  LOAD_ATTR             2  'begidx'
         122  LOAD_CONST            2  1
         125  INPLACE_ADD      
         126  ROT_TWO          
         127  STORE_ATTR            2  'begidx'

 192     130  BREAK_LOOP       
         131  JUMP_BACK            61  'to 61'
       134_0  COME_FROM                '111'
         134  POP_TOP          
         135  JUMP_BACK            61  'to 61'
         138  POP_TOP          
         139  POP_BLOCK        
       140_0  COME_FROM                '58'

 193     140  LOAD_GLOBAL           7  'ensure_str'
         143  LOAD_CONST            3  ''
         146  LOAD_ATTR             8  'join'
         149  LOAD_FAST             2  'buf'
         152  LOAD_FAST             0  'self'
         155  LOAD_ATTR             2  'begidx'
         158  LOAD_FAST             0  'self'
         161  LOAD_ATTR             3  'endidx'
         164  SLICE+3          
         165  CALL_FUNCTION_1       1 
         168  CALL_FUNCTION_1       1 
         171  STORE_FAST            3  'text'

 194     174  LOAD_GLOBAL           9  'log'
         177  LOAD_CONST            4  'complete text="%s"'
         180  LOAD_GLOBAL          10  'ensure_unicode'
         183  LOAD_FAST             3  'text'
         186  CALL_FUNCTION_1       1 
         189  BINARY_MODULO    
         190  CALL_FUNCTION_1       1 
         193  POP_TOP          

 195     194  LOAD_CONST            1  ''
         197  STORE_FAST            4  'i'

 196     200  SETUP_LOOP          119  'to 322'

 197     203  SETUP_EXCEPT         28  'to 234'

 198     206  LOAD_GLOBAL          10  'ensure_unicode'
         209  LOAD_FAST             0  'self'
         212  LOAD_ATTR             5  'completer'
         215  LOAD_FAST             3  'text'
         218  LOAD_FAST             4  'i'
         221  CALL_FUNCTION_2       2 
         224  CALL_FUNCTION_1       1 
         227  STORE_FAST            5  'r'
         230  POP_BLOCK        
         231  JUMP_FORWARD         20  'to 254'
       234_0  COME_FROM                '203'

 199     234  DUP_TOP          
         235  LOAD_GLOBAL          11  'IndexError'
         238  COMPARE_OP           10  'exception match'
         241  JUMP_IF_FALSE         8  'to 252'
         244  POP_TOP          
         245  POP_TOP          
         246  POP_TOP          
         247  POP_TOP          

 200     248  BREAK_LOOP       
         249  JUMP_FORWARD          2  'to 254'
         252  POP_TOP          
         253  END_FINALLY      
       254_0  COME_FROM                '231'

 201     254  LOAD_FAST             4  'i'
         257  LOAD_CONST            2  1
         260  INPLACE_ADD      
         261  STORE_FAST            4  'i'

 202     264  LOAD_FAST             5  'r'
         267  LOAD_CONST            0  ''
         270  COMPARE_OP            8  'is'
         273  JUMP_IF_FALSE         5  'to 281'
         276  POP_TOP          

 203     277  BREAK_LOOP       
         278  JUMP_BACK           203  'to 203'
       281_0  COME_FROM                '273'
         281  POP_TOP          

 204     282  LOAD_FAST             5  'r'
         285  JUMP_IF_FALSE        30  'to 318'
         288  POP_TOP          
         289  LOAD_FAST             5  'r'
         292  LOAD_FAST             1  'completions'
         295  COMPARE_OP            7  'not in'
         298  JUMP_IF_FALSE        17  'to 318'
         301  POP_TOP          

 205     302  LOAD_FAST             1  'completions'
         305  LOAD_ATTR            13  'append'
         308  LOAD_FAST             5  'r'
         311  CALL_FUNCTION_1       1 
         314  POP_TOP          
         315  JUMP_BACK           203  'to 203'
       318_0  COME_FROM                '298'
       318_1  COME_FROM                '285'
         318  POP_TOP          

 207     319  JUMP_BACK           203  'to 203'
       322_0  COME_FROM                '200'

 208     322  LOAD_GLOBAL           9  'log'
         325  LOAD_CONST            5  'text completions=<%s>'
         328  LOAD_GLOBAL          14  'map'
         331  LOAD_GLOBAL          10  'ensure_unicode'
         334  LOAD_FAST             1  'completions'
         337  CALL_FUNCTION_2       2 
         340  BINARY_MODULO    
         341  CALL_FUNCTION_1       1 
         344  POP_TOP          
         345  JUMP_FORWARD          1  'to 349'
       348_0  COME_FROM                '54'
         348  POP_TOP          
       349_0  COME_FROM                '345'

 209     349  LOAD_FAST             0  'self'
         352  LOAD_ATTR            15  'complete_filesystem'
         355  LOAD_CONST            6  'on'
         358  COMPARE_OP            2  '=='
         361  JUMP_IF_FALSE       313  'to 677'
         364  POP_TOP          
         365  LOAD_FAST             1  'completions'
         368  UNARY_NOT        
         369  JUMP_IF_FALSE       305  'to 677'
         372  POP_TOP          

 211     373  SETUP_LOOP           76  'to 452'
         376  LOAD_FAST             0  'self'
         379  LOAD_ATTR             2  'begidx'
         382  LOAD_CONST            1  ''
         385  COMPARE_OP            4  '>'
         388  JUMP_IF_FALSE        59  'to 450'
         391  POP_TOP          

 212     392  LOAD_FAST             0  'self'
         395  DUP_TOP          
         396  LOAD_ATTR             2  'begidx'
         399  LOAD_CONST            2  1
         402  INPLACE_SUBTRACT 
         403  ROT_TWO          
         404  STORE_ATTR            2  'begidx'

 213     407  LOAD_FAST             2  'buf'
         410  LOAD_FAST             0  'self'
         413  LOAD_ATTR             2  'begidx'
         416  BINARY_SUBSCR    
         417  LOAD_CONST            7  ' \t\n'
         420  COMPARE_OP            6  'in'
         423  JUMP_IF_FALSE        20  'to 446'
         426  POP_TOP          

 214     427  LOAD_FAST             0  'self'
         430  DUP_TOP          
         431  LOAD_ATTR             2  'begidx'
         434  LOAD_CONST            2  1
         437  INPLACE_ADD      
         438  ROT_TWO          
         439  STORE_ATTR            2  'begidx'

 215     442  BREAK_LOOP       
         443  JUMP_BACK           376  'to 376'
       446_0  COME_FROM                '423'
         446  POP_TOP          
         447  JUMP_BACK           376  'to 376'
         450  POP_TOP          
         451  POP_BLOCK        
       452_0  COME_FROM                '373'

 216     452  LOAD_GLOBAL           7  'ensure_str'
         455  LOAD_CONST            3  ''
         458  LOAD_ATTR             8  'join'
         461  LOAD_FAST             2  'buf'
         464  LOAD_FAST             0  'self'
         467  LOAD_ATTR             2  'begidx'
         470  LOAD_FAST             0  'self'
         473  LOAD_ATTR             3  'endidx'
         476  SLICE+3          
         477  CALL_FUNCTION_1       1 
         480  CALL_FUNCTION_1       1 
         483  STORE_FAST            3  'text'

 217     486  LOAD_GLOBAL           9  'log'
         489  LOAD_CONST            8  'file complete text="%s"'
         492  LOAD_GLOBAL          10  'ensure_unicode'
         495  LOAD_FAST             3  'text'
         498  CALL_FUNCTION_1       1 
         501  BINARY_MODULO    
         502  CALL_FUNCTION_1       1 
         505  POP_TOP          

 218     506  LOAD_GLOBAL          14  'map'
         509  LOAD_GLOBAL          10  'ensure_unicode'
         512  LOAD_GLOBAL          16  'glob'
         515  LOAD_ATTR            16  'glob'
         518  LOAD_GLOBAL          17  'os'
         521  LOAD_ATTR            18  'path'
         524  LOAD_ATTR            19  'expanduser'
         527  LOAD_FAST             3  'text'
         530  CALL_FUNCTION_1       1 
         533  LOAD_CONST            9  '*'
         536  BINARY_ADD       
         537  CALL_FUNCTION_1       1 
         540  CALL_FUNCTION_2       2 
         543  STORE_FAST            1  'completions'

 219     546  LOAD_FAST             0  'self'
         549  LOAD_ATTR            20  'mark_directories'
         552  LOAD_CONST           10  'on'
         555  COMPARE_OP            2  '=='
         558  JUMP_IF_FALSE        89  'to 650'
       561_0  THEN                     651
         561  POP_TOP          

 220     562  BUILD_LIST_0          0 
         565  STORE_FAST            6  'mc'

 221     568  SETUP_LOOP           70  'to 641'
         571  LOAD_FAST             1  'completions'
         574  GET_ITER         
         575  FOR_ITER             62  'to 640'
         578  STORE_FAST            7  'f'

 222     581  LOAD_GLOBAL          17  'os'
         584  LOAD_ATTR            18  'path'
         587  LOAD_ATTR            21  'isdir'
         590  LOAD_FAST             7  'f'
         593  CALL_FUNCTION_1       1 
         596  JUMP_IF_FALSE        24  'to 623'
         599  POP_TOP          

 223     600  LOAD_FAST             6  'mc'
         603  LOAD_ATTR            13  'append'
         606  LOAD_FAST             7  'f'
         609  LOAD_GLOBAL          17  'os'
         612  LOAD_ATTR            22  'sep'
         615  BINARY_ADD       
         616  CALL_FUNCTION_1       1 
         619  POP_TOP          
         620  JUMP_BACK           575  'to 575'
       623_0  COME_FROM                '596'
         623  POP_TOP          

 225     624  LOAD_FAST             6  'mc'
         627  LOAD_ATTR            13  'append'
         630  LOAD_FAST             7  'f'
         633  CALL_FUNCTION_1       1 
         636  POP_TOP          
         637  JUMP_BACK           575  'to 575'
         640  POP_BLOCK        
       641_0  COME_FROM                '568'

 226     641  LOAD_FAST             6  'mc'
         644  STORE_FAST            1  'completions'
         647  JUMP_FORWARD          1  'to 651'
       650_0  COME_FROM                '558'
         650  POP_TOP          
       651_0  COME_FROM                '647'

 227     651  LOAD_GLOBAL           9  'log'
         654  LOAD_CONST           11  'fnames=<%s>'
         657  LOAD_GLOBAL          14  'map'
         660  LOAD_GLOBAL          10  'ensure_unicode'
         663  LOAD_FAST             1  'completions'
         666  CALL_FUNCTION_2       2 
         669  BINARY_MODULO    
         670  CALL_FUNCTION_1       1 
         673  POP_TOP          
         674  JUMP_FORWARD          1  'to 678'
       677_0  COME_FROM                '369'
       677_1  COME_FROM                '361'
         677  POP_TOP          
       678_0  COME_FROM                '674'

 228     678  LOAD_FAST             1  'completions'
         681  RETURN_VALUE     

Parse error at or near `COME_FROM' instruction at offset 322_0

    def _display_completions(self, completions):
        if not completions:
            return
        self.console.write('\n')
        wmax = max(map(len, completions))
        w, h = self.console.size()
        cols = max(1, int((w - 1) / (wmax + 1)))
        rows = int(math.ceil(float(len(completions)) / cols))
        for row in range(rows):
            s = ''
            for col in range(cols):
                i = col * rows + row
                if i < len(completions):
                    self.console.write(completions[i].ljust(wmax + 1))

            self.console.write('\n')

        if in_ironpython:
            self.prompt = sys.ps1
        self._print_prompt()

    def complete(self, e):
        completions = self._get_completions()
        if completions:
            cprefix = commonprefix(completions)
            if len(cprefix) > 0:
                rep = [ c for c in cprefix ]
                point = self.l_buffer.point
                self.l_buffer[self.begidx:self.endidx] = rep
                self.l_buffer.point = point + len(rep) - (self.endidx - self.begidx)
            if len(completions) > 1:
                if self.show_all_if_ambiguous == 'on':
                    self._display_completions(completions)
                else:
                    self._bell()
        else:
            self._bell()
        self.finalize()

    def possible_completions(self, e):
        completions = self._get_completions()
        self._display_completions(completions)
        self.finalize()

    def insert_completions(self, e):
        completions = self._get_completions()
        b = self.begidx
        e = self.endidx
        for comp in completions:
            rep = [ c for c in comp ]
            rep.append(' ')
            self.l_buffer[b:e] = rep
            b += len(rep)
            e = b

        self.line_cursor = b
        self.finalize()

    def menu_complete(self, e):
        self.finalize()

    def insert_text(self, string):
        self.l_buffer.insert_text(string, self.argument_reset)
        self.finalize()

    def beginning_of_line(self, e):
        self.l_buffer.beginning_of_line()
        self.finalize()

    def end_of_line(self, e):
        self.l_buffer.end_of_line()
        self.finalize()

    def forward_char(self, e):
        self.l_buffer.forward_char(self.argument_reset)
        self.finalize()

    def backward_char(self, e):
        self.l_buffer.backward_char(self.argument_reset)
        self.finalize()

    def forward_word(self, e):
        self.l_buffer.forward_word(self.argument_reset)
        self.finalize()

    def backward_word(self, e):
        self.l_buffer.backward_word(self.argument_reset)
        self.finalize()

    def forward_word_end(self, e):
        self.l_buffer.forward_word_end(self.argument_reset)
        self.finalize()

    def backward_word_end(self, e):
        self.l_buffer.backward_word_end(self.argument_reset)
        self.finalize()

    def beginning_of_line_extend_selection(self, e):
        self.l_buffer.beginning_of_line_extend_selection()
        self.finalize()

    def end_of_line_extend_selection(self, e):
        self.l_buffer.end_of_line_extend_selection()
        self.finalize()

    def forward_char_extend_selection(self, e):
        self.l_buffer.forward_char_extend_selection(self.argument_reset)
        self.finalize()

    def backward_char_extend_selection(self, e):
        self.l_buffer.backward_char_extend_selection(self.argument_reset)
        self.finalize()

    def forward_word_extend_selection(self, e):
        self.l_buffer.forward_word_extend_selection(self.argument_reset)
        self.finalize()

    def backward_word_extend_selection(self, e):
        self.l_buffer.backward_word_extend_selection(self.argument_reset)
        self.finalize()

    def forward_word_end_extend_selection(self, e):
        self.l_buffer.forward_word_end_extend_selection(self.argument_reset)
        self.finalize()

    def backward_word_end_extend_selection(self, e):
        self.l_buffer.forward_word_end_extend_selection(self.argument_reset)
        self.finalize()

    def upcase_word(self, e):
        self.l_buffer.upcase_word()
        self.finalize()

    def downcase_word(self, e):
        self.l_buffer.downcase_word()
        self.finalize()

    def capitalize_word(self, e):
        self.l_buffer.capitalize_word()
        self.finalize()

    def clear_screen(self, e):
        self.console.page()
        self.finalize()

    def redraw_current_line(self, e):
        self.finalize()

    def accept_line(self, e):
        self.finalize()
        return True

    def delete_char(self, e):
        self.l_buffer.delete_char(self.argument_reset)
        self.finalize()

    def backward_delete_char(self, e):
        self.l_buffer.backward_delete_char(self.argument_reset)
        self.finalize()

    def backward_delete_word(self, e):
        self.l_buffer.backward_delete_word(self.argument_reset)
        self.finalize()

    def forward_delete_word(self, e):
        self.l_buffer.forward_delete_word(self.argument_reset)
        self.finalize()

    def delete_horizontal_space(self, e):
        self.l_buffer.delete_horizontal_space()
        self.finalize()

    def self_insert(self, e):
        if e.char and ord(e.char) != 0:
            self.insert_text(e.char)
        self.finalize()

    def paste(self, e):
        if self.enable_win32_clipboard:
            txt = clipboard.get_clipboard_text_and_convert(False)
            txt = txt.split('\n')[0].strip('\r').strip('\n')
            log('paste: >%s<' % map(ord, txt))
            self.insert_text(txt)
        self.finalize()

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
                log('multi: >%s<' % self.paste_line_buffer)
                return True
            return False
        self.finalize()

    def ipython_paste(self, e):
        if self.enable_win32_clipboard:
            txt = clipboard.get_clipboard_text_and_convert(self.enable_ipython_paste_list_of_lists)
            if self.enable_ipython_paste_for_paths:
                if len(txt) < 300 and '\t' not in txt and '\n' not in txt:
                    txt = txt.replace('\\', '/').replace(' ', '\\ ')
            self.insert_text(txt)
        self.finalize()

    def copy_region_to_clipboard(self, e):
        self.l_buffer.copy_region_to_clipboard()
        self.finalize()

    def copy_selection_to_clipboard(self, e):
        self.l_buffer.copy_selection_to_clipboard()
        self.finalize()

    def cut_selection_to_clipboard(self, e):
        self.l_buffer.cut_selection_to_clipboard()
        self.finalize()

    def dump_functions(self, e):
        print
        txt = '\n'.join(self.rl_settings_to_string())
        print txt
        self._print_prompt()
        self.finalize()


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