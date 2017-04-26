# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
OPEN_RES_FLAG_USE_ARCH = 1
OPEN_RES_FLAG_USE_OS = 2
OPEN_RES_FLAG_USE_COMPILED = 4
OPEN_RES_FLAG_USE_LIBC = 8

def GetDir(subdir=None):
    import mcl_platform.tasking.resource
    return mcl_platform.tasking.resource.GetDir(subdir)


def GetName(resName=None):
    import mcl_platform.tasking.resource
    return mcl_platform.tasking.resource.GetName(resName)


def Open(filename, flags, subdir=None, project=None):
    import mcl_platform.tasking.resource
    return mcl_platform.tasking.resource.Open(filename, flags, subdir, project)