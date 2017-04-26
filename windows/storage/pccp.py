# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: pccp.py
# Compiled at: 2012-10-12 14:52:57
import socket
import ssl
import asyncore
import os
from collections import deque
BEWARE_OF_DOG = '**   **    **    ******   **   **  **  **   **   *****   !!\n**   **   ****   **   **  ***  **  **  ***  **  **       !!\n** * **  **  **  ******   ** * **  **  ** * **  **  ***  !!\n *****   ******  **  *    **  ***  **  **  ***  **   **\n ** **   **  **  **   **  **   **  **  **   **   *****   !!\n\n                 DO NOT CLOSE THIS WINDOW\n                            or\n            you *WILL* lose your connection to\n\n%s\n\n'
DOG_WIDTH = 60

def identity(data):
    return data


def http_chunk(data):
    return '%x\r\n%s\r\n' % (len(data), data)


class _http_unchunk(object):

    def __init__(self):
        self.length = None
        self.buff = ''
        return

    def _decode(self):
        chunk = self.buff[:self.length]
        clen = len(chunk)
        if clen < self.length:
            self.length -= clen
            self.buff = ''
        else:
            self.buff = self.buff[clen:]
            self.length = None
        return chunk

    def __call__(self, data):
        self.buff += data
        if self.length is None:
            if self.buff.startswith('\r\n'):
                self.buff = self.buff[2:]
            bits = self.buff.split('\r\n', 1)
            if len(bits) == 1:
                return
            self.length = int(bits[0], 16)
            self.buff = bits[1]
            return self._decode()
        else:
            return self._decode()
        return


http_unchunk = _http_unchunk()

class Channel(asyncore.dispatcher):
    BLOCK_SIZE = 4096

    def __init__(self, name, sock, counterpart=None, filter=identity):
        asyncore.dispatcher.__init__(self, sock=sock)
        self.rbuff = deque()
        self.sbuff = deque()
        self.name = name
        self.counterpart = counterpart
        self.filter = filter
        self.filtering = False
        self.live = True

    def handle_close(self):
        if self.live:
            print 'Shutdown initiated by %s end of channel.' % self.name
            self.close()
            self.live = False
            if self.counterpart and self.counterpart.live:
                self.counterpart.close()

    def handle_read(self):
        block = self.recv(self.BLOCK_SIZE)
        if block:
            if self.counterpart:
                self.counterpart.push(block)
            else:
                self.rbuff.append(block)

    def handle_write(self):
        buff = self.sbuff.popleft()
        tosend = len(buff)
        sent = self.send(buff)
        if sent < tosend:
            self.sbuff.appendleft(buff[sent:])

    def writable(self):
        return len(self.sbuff) > 0

    def pair(self, counterpart):
        if self.counterpart is None:
            self.counterpart = counterpart
        else:
            raise Exception('Cannot pair with %s; already paired with %s!' % (counterpart, self.counterpart))
        while self.rbuff:
            self.counterpart.push(self.rbuff.popleft())

        return

    def push(self, data):
        if self.filtering:
            data = self.filter(data)
            if data is None:
                return
        self.sbuff.append(data)
        return


def pair_channels(A, B):
    A.pair(B)
    B.pair(A)


class CmdChannel(asyncore.dispatcher):

    def __init__(self, cmd_socket, *channels):
        asyncore.dispatcher.__init__(self, sock=cmd_socket)
        self.channels = channels
        self.done = False

    def readable(self):
        return not self.done

    def handle_read(self):
        blah = self.recv(2)
        if blah:
            print 'CMD channel received handoff trigger; CMD channel closing...'
            for ch in self.channels:
                ch.filtering = True

            self.done = True

    def writable(self):
        return self.done

    def handle_write(self):
        if self.done:
            self.send('OK')

    def handle_close(self):
        self.close()
        print '(CMD channel has closed)\n'


def import_filter(full_name):
    path, name = full_name.rsplit('.', 1)
    mod = __import__(path, globals(), locals(), [name])
    return getattr(mod, name)


def connect(hostname, portname, use_ssl=False):
    names = socket.getaddrinfo(hostname, portname)
    fam, typ, pro, can, addr = names[0]
    S = socket.socket(fam, typ, pro)
    if use_ssl:
        S = ssl.wrap_socket(S)
    S.connect(addr)
    return S


def main():
    import sys
    import optparse
    OP = optparse.OptionParser(usage='usage: %prog [OPTIONS] TARGET_HOST TARGET_PORT LOCAL_CMD_PORT LOCAL_DATA_PORT')
    OP.add_option('-s', '--ssl', default=False, action='store_true', dest='ssl', help='Use SSL to connect to TARGET_HOST:TARGET_PORT')
    OP.add_option('-u', '--upstream', default=None, dest='upstream', metavar='MODULE.NAME', help='Import/use the named callable to filter upstream (proxy -> target) data.')
    OP.add_option('-d', '--downstream', default=None, dest='downstream', metavar='MODULE.NAME', help='Import/use the named callable to filter downstream (target -> proxy) data.')
    opts, args = OP.parse_args()
    if len(args) != 4:
        OP.error('Missing required arguments...')
    if opts.upstream:
        try:
            filter_up = import_filter(opts.upstream)
        except Exception, x:
            OP.error("Failed to import filter '%s' (%s)" % (opts.upstream, x))

    else:
        filter_up = identity
    if opts.downstream:
        try:
            filter_down = import_filter(opts.downstream)
        except Exception, x:
            OP.error("Failed to import filter '%s' (%s)" % (opts.downstream, x))

    else:
        filter_down = identity
    endpoint = '%s:%s' % (args[0], args[1])
    print BEWARE_OF_DOG % endpoint.center(DOG_WIDTH)
    print '*** ESTABLISHING DATA/CMD CHANNELS ***'
    print 'IMPLANT -> %s:%s' % (args[0], args[1])
    implant_sock = connect(args[0], args[1], opts.ssl)
    print 'CMD     -> 127.0.0.1:%s' % args[2]
    cmd_sock = connect('127.0.0.1', args[2])
    print 'PROXY   -> 127.0.0.1:%s' % args[3]
    proxy_sock = connect('127.0.0.1', args[3])
    implant_channel = Channel('IMPLANT', implant_sock, filter=filter_up)
    proxy_channel = Channel('PROXY', proxy_sock, filter=filter_down)
    pair_channels(implant_channel, proxy_channel)
    cmd_channel = CmdChannel(cmd_sock, implant_channel, proxy_channel)
    print '*** DATA/CMD CHANNELS ESTABLISHED ***\n'
    asyncore.loop()
    return


if __name__ == '__main__':
    import traceback
    try:
        main()
    except SystemExit:
        raise
    except:
        traceback.print_exc()

    if 'PCCP_NO_DELAY' not in os.environ:
        raw_input('\n[All connections dead; press ENTER to terminate...]')