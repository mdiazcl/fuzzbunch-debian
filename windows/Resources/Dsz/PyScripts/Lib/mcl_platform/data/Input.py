# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Input.py


def GetInput(InputFilename):
    import _dsz
    import array
    import mcl.object.MclTime
    import mcl.data.DataHandlerInput
    input = mcl.data.DataHandlerInput.DataHandlerInput()
    input.SetMessageType(_dsz.dszObj.dsz_dh_get_msgtype())
    input.SetStatus(_dsz.dszObj.dsz_dh_get_status())
    input.SetDest(_dsz.dszObj.dsz_dh_get_dest())
    input.SetPriority(_dsz.dszObj.dsz_dh_get_priority())
    input.SetProducerInterface(_dsz.dszObj.dsz_dh_get_prodiface())
    input.SetProducerProvider(_dsz.dszObj.dsz_dh_get_prodprovider())
    input.SetTaskIds(_dsz.dszObj.dsz_dh_get_taskids())
    input.SetUuid(_dsz.dszObj.dsz_dh_get_uuid())
    data = _dsz.dszObj.dsz_dh_get_data()
    aData = array.array('B')
    for item in data:
        aData.append(item)

    input.SetData(aData)
    collectTime = _dsz.dszObj.dsz_dh_get_collecttime()
    input.SetCollectTime(mcl.object.MclTime.MclTime(collectTime['seconds'], collectTime['nanoseconds'], collectTime['type']))
    return input