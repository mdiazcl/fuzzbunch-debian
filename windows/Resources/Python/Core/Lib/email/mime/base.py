# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: base.py
"""Base class for MIME specializations."""
__all__ = [
 'MIMEBase']
from email import message

class MIMEBase(message.Message):
    """Base class for MIME specializations."""

    def __init__(self, _maintype, _subtype, **_params):
        """This constructor adds a Content-Type: and a MIME-Version: header.
        
        The Content-Type: header is taken from the _maintype and _subtype
        arguments.  Additional parameters for this header are taken from the
        keyword arguments.
        """
        message.Message.__init__(self)
        ctype = '%s/%s' % (_maintype, _subtype)
        self.add_header('Content-Type', ctype, **_params)
        self['MIME-Version'] = '1.0'