# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\pyreadline\release.py
# Compiled at: 2011-10-07 03:26:06
name = 'pyreadline'
branch = ''
version = '1.7.1'
revision = '$Revision$'
description = 'A python implmementation of GNU readline.'
long_description = '\nThe pyreadline package is a python implementation of GNU readline functionality\nit is based on the ctypes based UNC readline package by Gary Bishop. \nIt is not complete. It has been tested for use with windows 2000 and windows xp.\n\nVersion 1.7.1 includes fixes for 64-bit windows, thanks to Christoph Gohlke for\nhelping out.\n\nVersion 1.7 will be the last release with compatibility with 2.4 and 2.5. The next\nmajor release will target 2.6, 2.7 and 3.x. The 1.7 series will only receive bugfixes\nfrom now on.\n\nFeatures:\n *  keyboard text selection and copy/paste\n *  Shift-arrowkeys for text selection\n *  Control-c can be used for copy activate with allow_ctrl_c(True) in config file\n *  Double tapping ctrl-c will raise a KeyboardInterrupt, use ctrl_c_tap_time_interval(x)\n    where x is your preferred tap time window, default 0.3 s.\n *  paste pastes first line of content on clipboard. \n *  ipython_paste, pastes tab-separated data as list of lists or numpy array if all data is numeric\n *  paste_mulitline_code pastes multi line code, removing any empty lines.\n \n \n The latest development version is always available at the IPython subversion\n repository_.\n\n.. _repository:\n '
license = 'BSD'
authors = {'Jorgen': ('Jorgen Stenarson', 'jorgen.stenarson@bostream.nu'),'Gary': ('Gary Bishop', ''),
   'Jack': ('Jack Trainor', '')
   }
url = 'http://ipython.scipy.org/moin/PyReadline/Intro'
download_url = 'https://launchpad.net/pyreadline/+download'
platforms = [
 'Windows XP/2000/NT',
 'Windows 95/98/ME']
keywords = [
 'readline',
 'pyreadline']
classifiers = [
 'Development Status :: 5 - Production/Stable',
 'Environment :: Console',
 'Operating System :: Microsoft :: Windows',
 'License :: OSI Approved :: BSD License',
 'Programming Language :: Python :: 2.4',
 'Programming Language :: Python :: 2.5',
 'Programming Language :: Python :: 2.6',
 'Programming Language :: Python :: 2.7']