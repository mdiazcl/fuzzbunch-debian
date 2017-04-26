# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: CpAddress.py


class CpAddress:

    def __init__(self, addr):
        self.address = addr

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return CpAddress.IntToDotted(self.address)

    def __copy__(self):
        return CpAddress(self.address)

    def __deepcopy__(self, memo):
        return CpAddress(self.address)

    def GetAddress(self):
        return self.address

    def SetAddress(self, addr):
        self.address = addr

    def DottedToInt(stringAddr):
        if stringAddr.startswith('z'):
            stringAddr = stringAddr[1:]
        listIntAddr = stringAddr.split('.')
        intAddr = int('%02x%02x%02x%02x' % (int(listIntAddr[0]), int(listIntAddr[1]), int(listIntAddr[2]), int(listIntAddr[3])), 16)
        return intAddr

    def IntToDotted(intAddr):
        return 'z%u.%u.%u.%u' % (intAddr >> 24 & 255,
         intAddr >> 16 & 255,
         intAddr >> 8 & 255,
         intAddr & 255)

    DottedToInt = staticmethod(DottedToInt)
    IntToDotted = staticmethod(IntToDotted)


class CpCidrAddress:

    def __init__(self, addr, mask):
        self.SetAddress(addr, mask)

    def __repr__(self):
        return '%s/%u' % (CpAddress.IntToDotted(self.address), self.bits)

    def __copy__(self):
        return CpCidrAddress(self.address, self.mask)

    def __deepcopy__(self, memo):
        return CpCidrAddress(self.address, self.mask)

    def GetAddress(self):
        return (
         self.address, self.bits, self.mask)

    def SetAddress(self, addr, mask):
        self.address = addr
        self.mask = mask
        self.bits = 0
        while mask:
            self.bits = self.bits + 1
            mask = mask << 1 & 4294967295