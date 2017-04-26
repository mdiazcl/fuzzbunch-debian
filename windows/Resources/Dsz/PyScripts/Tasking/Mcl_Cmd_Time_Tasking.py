# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_Time_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.time', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.time.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.status.cmd.time.Params()
    if lpParams['target'] != None:
        tgtParams.target = lpParams['target']
    taskXml = mcl.tasking.Tasking()
    if len(tgtParams.target) > 0:
        taskXml.SetTargetRemote(lpParams['target'])
    else:
        taskXml.SetTargetLocal()
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    rpc = mca.status.cmd.time.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.status.cmd.time.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)