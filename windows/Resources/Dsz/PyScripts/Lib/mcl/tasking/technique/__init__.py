# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
TECHNIQUE_PROVIDER_ANY = 0
TECHNIQUE_MCL_INJECT = 'Mcl_ThreadInject'
TECHNIQUE_MCL_MEMORY = 'Mcl_Memory'
TECHNIQUE_MCL_PRIVILEGE = 'Mcl_Privilege'
TECHNIQUE_MCL_NTNATIVEAPI = 'Mcl_NtNativeApi'

def Lookup(cmdName, ifaceName, desiredTechnique):
    import mcl_platform.tasking.technique
    if len(ifaceName) == 0:
        return TECHNIQUE_PROVIDER_ANY
    else:
        fullTech = '_PROV_%s' % ifaceName
        if desiredTechnique != None and len(desiredTechnique) > 0:
            rtn, provider = mcl_platform.tasking.technique.Lookup(fullTech, desiredTechnique)
            if not rtn:
                raise RuntimeError("Lookup for technique '%s' failed" % desiredTechnique)
            return provider
        if cmdName != None and len(cmdName) > 0:
            rtn, provider = mcl_platform.tasking.technique.Lookup(fullTech, cmdName)
            if rtn:
                return provider
        rtn, provider = mcl_platform.tasking.technique.Lookup(fullTech, 'Default')
        if not rtn:
            return TECHNIQUE_PROVIDER_ANY
        return provider
        return