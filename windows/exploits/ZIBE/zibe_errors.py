# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\zibe_errors.py
# Compiled at: 2013-03-28 21:23:50
error_codes = {3758096385: [
              'ZB_ERROR_NOMEMORY', 'Out of memory'],
   3758096386: [
              'ZB_ERROR_INVALID_HANDLE', 'The provided handle is not valid'],
   3758096387: [
              'ZB_ERROR_INVALID_ARGUMENT', 'Invalid argument'],
   3758096388: [
              'ZB_ERROR_SESSION_ALREADY_INITIALIZED', 'StartSession can only be called once'],
   3758096389: [
              'ZB_ERROR_UNEXPECTED', 'Catastrophic Failure'],
   3758096390: [
              'ZB_ERROR_MISSING_PARAMETER', 'One or more parameters is missing'],
   3758096391: [
              'ZB_ERROR_NO_SHARE_SELECTED', 'No share was selected'],
   3758096392: [
              'ZB_ERROR_PATH_TOO_LONG', 'The specified path is too long'],
   3758096393: [
              'ZB_ERROR_INVALID_PATH', 'The provided path is invalid'],
   3758096394: [
              'ZB_ERROR_INVALID_HANDLE', 'Out of memory'],
   3758096425: [
              'ZB_ERROR_ESRO_FAILED', 'Failed to ESRO'],
   3758096426: [
              'ZB_ERROR_DAPU_FAILED', 'Failed to DAPU'],
   2: [
     'ErrorFileNotFound', 'The system cannot find the file specified. '],
   3: [
     'ErrorPathNotFound', 'The system cannot find the path specified. '],
   5: [
     'ErrorAccessDenied', 'Access is denied. '],
   50: [
      'ErrorNotSupported', 'The request is not supported. '],
   123: [
       'ErrorBadFile', 'The filename, directory name, or volume label syntax is incorrect'],
   259: [
       'ErrorStatusPending', 'No more data is available. '],
   1051: [
        'ErrorDependentServicesRunning', 'Service error: A stop control has been sent to a service that other running services are dependent on.'],
   1052: [
        'ErrorInvalidServiceControl', 'Service error: The requested control is not valid for this service'],
   1056: [
        'ErrorServiceRunning', 'Service error: An instance of the service is already running'],
   1060: [
        'ErrorServiceDoesNotExist', 'Service error: The specified service does not exist as an installed service.'],
   1062: [
        'ErrorServiceNotActive', 'Service error: The specified service is not running'],
   1330: [
        'ErrorPasswordExpired', 'Logon failure: the specified account password has expired. '],
   1331: [
        'ErrorAccountDisabled', 'Logon failure: account currently disabled. '],
   1745: [
        'ErrorRpcOpnumOutOfRange', 'The procedure number is out of range. '],
   1767: [
        'ErrorRpcZeroDivide', 'The RPC server attempted an integer division by zero. '],
   1769: [
        'ErrorRpcFpZeroDivide', 'A floating-point operation at the RPC server caused a division by zero. '],
   1780: [
        'ErrorRpcNullRefPtr', 'A null reference pointer was passed to the stub. '],
   1781: [
        'ErrorRpcEnumOutOfRange', 'The enumeration value is out of range. '],
   1782: [
        'ErrorRpcByteCountTooSmall', 'The byte count is too small. '],
   1783: [
        'ErrorRpcBadStub', 'The stub received bad data. '],
   1792: [
        'ErrorNetlogonNotStarted', 'An attempt was made to logon, but the network logon service was not started. '],
   1793: [
        'ErrorAccountExpired', 'The users account has expired. '],
   1796: [
        'ErrorUnknownPort', 'The specified port is unknown. '],
   1797: [
        'ErrorUnknownPrinterDriver', 'The print driver is unknown. '],
   1798: [
        'ErrorUnknownPrintProcessor', 'The print processor is unknown. '],
   1801: [
        'ErrorInvalidPrinterName', 'The printer name is invalid. '],
   1803: [
        'ErrorInvalidPrinterCommand', 'The printer command is invalid. '],
   1817: [
        'ErrorNoInterfaces', 'No interfaces have been registered. '],
   1818: [
        'ErrorCallCancelled', 'The remote procedure call was cancelled. '],
   1819: [
        'ErrorBindingIncomplete', 'The binding handle does not contain all required information. '],
   1820: [
        'ErrorCommFailure', 'A communications failure occurred during a remote procedure call. '],
   1821: [
        'ErrorUnsupportedAuthLevel', 'The requested authentication level is not supported. '],
   1822: [
        'ErrorNoPrincipalNameRegistered', 'No principal name registered. '],
   1823: [
        'ErrorNotRpcErrCode', 'The error specified is not a valid Windows RPC error code. '],
   1825: [
        'ErrorSecPackageError', 'A security package specific error occurred. '],
   1829: [
        'ErrorWrongStubVersion', 'Incompatible version of the RPC stub. '],
   1916: [
        'ErrorPipeClosed', 'The RPC pipe object has already been closed. '],
   1918: [
        'ErrorPipeEmpty', 'No more data is available from the RPC pipe. '],
   1931: [
        'ErrorContextExpired', 'The context has expired and can no longer be used. '],
   16777217: [
            'DosErrorInvalidFunction', 'Incorrect function. '],
   16777218: [
            'DosErrorInvalidFile', 'The system cannot find the file specified. '],
   16777219: [
            'DosErrorInvalidPath', 'The system cannot find the path specified. '],
   16777220: [
            'DosErrorTooManyOpenFiles', 'The system cannot open the file. '],
   16777221: [
            'DosErrorAccessDenied', 'Access is denied. '],
   16777222: [
            'DosErrorInvalidHandle', 'The handle is invalid. '],
   16777231: [
            'DosErrorInvalidDrive', 'The system cannot find the drive specified. '],
   16777266: [
            'DosErrorNotSupported', 'The request is not supported. '],
   16777267: [
            'DosErrorRemoteNotListening', 'Windows cannot find the network path. Verify that the network path is correct and the destination computer is not busy or turned off. If Windows still cannot find the network path, contact your network administrator. '],
   16777268: [
            'DosErrorDuplicateName', 'You were not connected because a duplicate name exists on the network. If joining a domain, go to System in Control Panel to change the computer name and try again. If joining a workgroup, choose another workgroup name. '],
   16777269: [
            'DosErrorBadNetPath', 'The network path was not found. '],
   16777270: [
            'DosErrorNetworkBusy', 'The network is busy. '],
   16777271: [
            'DosErrorDeviceNotExist', 'The specified network resource or device is no longer available. '],
   16777272: [
            'DosErrorTooManyCmds', 'The network BIOS command limit has been reached.'],
   16777273: [
            'DosErrorAdapterHardwareError', 'A network adapter hardware error occurred. '],
   16777274: [
            'DosErrorBadNetworkResponse', 'The specified server cannot perform the requested operation. '],
   16777275: [
            'DosErrorUnexpectedNetError', 'An unexpected network error occurred. '],
   16777276: [
            'DosErrorBadRemoteAdapter', 'The remote adapter is not compatible. '],
   16777277: [
            'DosErrorPrintQFull', 'The printer queue is full. '],
   16777278: [
            'DosErrorNoSpoolSpace', 'Space to store the file waiting to be printed is not available on the server. '],
   16777279: [
            'DosErrorPrintCancelled', 'Your file waiting to be printed was deleted. '],
   16777280: [
            'DosErrorNetNameDeleted', 'The specified network name is no longer available. '],
   16777281: [
            'DosErrorNetworkAccessDenied', 'Network access is denied. '],
   16777282: [
            'DosErrorBadDeviceType', 'The network resource type is not correct. '],
   16777283: [
            'DosErrorBadNetName', 'The network name cannot be found. '],
   16777284: [
            'DosErrorTooManyNames', 'The name limit for the local computer network adapter card was exceeded. '],
   16777285: [
            'DosErrorTooManySessions', 'The network BIOS session limit was exceeded. '],
   16777286: [
            'DosErrorSharingPaused', 'The remote server has been paused or is in the process of being started. '],
   16777287: [
            'DosErrorRequestNotAccepted', 'No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept. '],
   16777288: [
            'DosErrorRedirPaused', 'The specified printer or disk device has been paused. '],
   16777304: [
            'DosErrorNetWriteFault', 'A write fault occurred on the network. '],
   16777446: [
            'DosErrorBadPipe', 'The pipe state is invalid. '],
   16777447: [
            'DosErrorPipeBusy', 'All pipe instances are busy. '],
   16777448: [
            'DosErrorNoData', 'The pipe is being closed. '],
   16777449: [
            'DosErrorPipeNotConnected', 'No process is on the other end of the pipe. '],
   16777450: [
            'DosErrorMoreData', 'More data is available. '],
   16777456: [
            'DosErrorVcDisconnected', 'The session was canceled. '],
   2952790017: [
              'TbErrorAbort', 'TIBE had to abort'],
   2952790018: [
              'TbErrorSocketInvalid', 'Invalid socket'],
   2952790019: [
              'TbErrorBadProtocol', 'Bad protocol specified or detected'],
   2952790020: [
              'TbErrorCantconnect', 'Cannot connect to target'],
   2952790021: [
              'TbErrorAckFin', 'The socket closed on the remote end'],
   2952790022: [
              'TbErrorSendFailed', 'The send call failed'],
   2952790023: [
              'TbErrorRecvFailed', 'The recv call failed'],
   2952790024: [
              'TbErrorTimeout', 'The operation timed out'],
   2952790032: [
              'TbErrorBadPacket', 'The packet format is invalid'],
   2952790064: [
              'TbErrorNomemory', 'Out of memory'],
   2952790080: [
              'TbErrorBadParam', 'Bad parameter passed to a function'],
   2952790081: [
              'TbErrorFailed', 'A generic failure occurred'],
   2952794153: [
              'KrbErrorApModified', 'Kerberos ticket modified'],
   3221225473: [
              'NtErrorUnsuccessful', 'The requested operation was unsuccessful. '],
   3221225474: [
              'NtErrorNotImplemented', 'The requested operation is not implemented. '],
   3221225475: [
              'NtErrorInvalidInfoClass', 'The specified information class is not a valid information class for the specified object. '],
   3221225476: [
              'NtErrorInfoLengthMismatch', 'The specified information record length does not match the length required for the specified information class. '],
   3221225477: [
              'NtErrorAccessViolation', 'Invalid Memory Access'],
   3221225478: [
              'NtErrorInPageError', 'The instruction at 0x%p referenced memory at 0x%p. The required data was not placed into memory because of an I/O error status of 0x%x. '],
   3221225479: [
              'NtErrorPageFileQuota', 'The pagefile quota for the process has been exhausted. '],
   3221225480: [
              'NtErrorInvalidHandle', 'An invalid HANDLE was specified. '],
   3221225481: [
              'NtErrorBadInitStack', 'An invalid initial stack was specified in a call to NtCreateThread. '],
   3221225482: [
              'NtErrorBadInitPc', 'An invalid initial start address was specified in a call to NtCreateThread. '],
   3221225483: [
              'NtErrorInvalidCid', 'An invalid Client ID was specified. '],
   3221225484: [
              'NtErrorTimerNotCanceled', 'An attempt was made to cancel or set a timer that has an associated APC and the subject thread is not the thread that originally set the timer with an associated APC routine. '],
   3221225485: [
              'NtErrorInvalidParameter', 'An invalid parameter was passed to a service or function. '],
   3221225486: [
              'NtErrorNoSuchDevice', 'A device which does not exist was specified.'],
   3221225487: [
              'NtErrorNoSuchFile', '{File Not Found} The file does not exist. '],
   3221225488: [
              'NtErrorInvalidDeviceRequest', 'The specified request is not a valid operation for the target device. '],
   3221225489: [
              'NtErrorEndOfFile', 'The end-of-file marker has been reached. There is no valid data in the file beyond this marker. '],
   3221225494: [
              'NtErrorMoreProcessingRequired', ''],
   3221225506: [
              'NtErrorAccessDenied', 'Access Denied: A process has requested access to an object, but has not been granted those access rights. '],
   3221225508: [
              'NtErrorObjectTypeMismatch', 'There is a mismatch between the type of object required by the requested operation and the type of object that is specified in the request. '],
   3221225511: [
              'NtErrorUnwindException', 'Unwind exception code.'],
   3221225523: [
              'NtErrorObjectNameInvalid', 'Object Name invalid. '],
   3221225524: [
              'NtErrorObjectNameNotFound', 'Object Name not found. '],
   3221225525: [
              'NtErrorDuplicateNameConflict', 'Object Name already exists. '],
   3221225527: [
              'NtErrorPortDisconnected', 'Attempt to send a message to a disconnected communication port. '],
   3221225529: [
              'NtErrorObjectPathInvalid', 'Object Path Component was not a directory object.'],
   3221225530: [
              'NtErrorObjectPathNotFound', ' The path does not exist. '],
   3221225531: [
              'NtErrorObjectPathSyntaxBad', 'Object Path Component was not a directory object.'],
   3221225539: [
              'NtErrorSharingViolation', 'A file cannot be opened because the share access flags are incompatible. '],
   3221225556: [
              'NtErrorLockConflict', 'A requested read/write cannot be granted due to a conflicting file lock. '],
   3221225557: [
              'NtErrorLockNotGranted', 'A requested file lock cannot be granted due to other existing locks. '],
   3221225558: [
              'NtErrorDeletePending', 'A non close operation has been requested of a file object with a delete pending. '],
   3221225562: [
              'NtErrorInvalidOwner', 'Indicates a particular Security ID may not be assigned as the owner of an object. '],
   3221225563: [
              'NtErrorInvalidPrimaryGroup', 'Indicates a particular Security ID may not be assigned as the primary group of an object. '],
   3221225564: [
              'NtErrorNoImpersonationToken', 'An attempt has been made to operate on an impersonation token by a thread that is not currently impersonating a client. '],
   3221225565: [
              'NtErrorCantDisableMandatory', 'A mandatory group may not be disabled. '],
   3221225566: [
              'NtErrorNoLogonServers', 'There are currently no logon servers available to service the logon request. '],
   3221225567: [
              'NtErrorNoLogonSession', 'A specified logon session does not exist. It may already have been terminated. '],
   3221225568: [
              'NtErrorNoSuchPrivilege', 'A specified privilege does not exist. '],
   3221225569: [
              'NtErrorPrivilegeNotHeld', 'A required privilege is not held by the client. '],
   3221225570: [
              'NtErrorInvalidAccountName', 'The name provided is not a properly formed account name. '],
   3221225571: [
              'NtErrorUserAlreadyExists', 'The specified account already exists. '],
   3221225572: [
              'NtErrorNoSuchUser', 'The specified account does not exist. '],
   3221225573: [
              'NtErrorGroupAlreadyExists', 'The specified group already exists. '],
   3221225574: [
              'NtErrorNoSuchGroup', 'The specified group does not exist. '],
   3221225575: [
              'NtErrorMemberInGroup', 'The specified user account is already in the specified group account. Also used to indicate a group cannot be deleted because it contains a member. '],
   3221225576: [
              'NtErrorMemberNotInGroup', 'The specified user account is not a member of the specified group account. '],
   3221225577: [
              'NtErrorLastAdminAccount', ' The requested operation would disable or delete the last remaining administration account. This is not allowed to prevent creating a situation in which the system cannot be administrated. '],
   3221225578: [
              'NtErrorWrongPassword', 'When trying to update a password, this return status indicates that the value provided as the current password is not correct. '],
   3221225579: [
              'NtErrorIllformedPassword', 'When trying to update a password, this return status indicates that the value provided for the new password contains values that are not allowed in passwords. '],
   3221225580: [
              'NtErrorPasswordRestriction', 'When trying to update a password, this status indicates that some password update rule has been violated. For example, the password may not meet length criteria. '],
   3221225581: [
              'NtErrorLogonFailure', 'The attempted logon is invalid. This is either due to a bad username or authentication information. '],
   3221225585: [
              'NtErrorPasswordExpired', 'The user accounts password has expired. '],
   3221225599: [
              'NtErrorDiskFull', 'An operation failed because the disk was full.'],
   3221225624: [
              'NtErrorFileInvalid', 'The volume for a file has been externally altered such that the opened file is no longer valid. '],
   3221225626: [
              'NtErrorInsufficientResources', 'Insufficient system resources exist to complete the API. '],
   3221225637: [
              'NtErrorBadImpersonationLevel', 'A specified impersonation level is invalid. Also used to indicate a required impersonation level was not provided. '],
   3221225638: [
              'NtErrorCantOpenAnonymous', 'An attempt was made to open an Anonymous level token. Anonymous tokens may not be opened. '],
   3221225644: [
              'NtErrorPipeNotAvailable', 'An instance of a named pipe cannot be found in the listening state. '],
   3221225645: [
              'NtErrorInvalidPipeState', 'The named pipe is not in the connected or closing state. '],
   3221225646: [
              'NtErrorPipeBusy', 'The specified pipe is set to complete operations and there are current I/O operations queued so it cannot be changed to queue operations. '],
   3221225647: [
              'NtErrorIllegalFunction', 'The specified handle is not open to the server end of the named pipe.'],
   3221225648: [
              'NtErrorPipeDisconnected', 'The specified named pipe is in the disconnected state. '],
   3221225649: [
              'NtErrorPipeClosing', 'The specified named pipe is in the closing state'],
   3221225650: [
              'NtErrorPipeConnected', 'The specified named pipe is in the connected state.'],
   3221225651: [
              'NtErrorPipeListening', 'The specified named pipe is in the listening state. '],
   3221225654: [
              'NtErrorFileForcedClosed', 'The specified file has been closed by another process. '],
   3221225658: [
              'NtErrorFileIsDirectory', 'The file that was specified as a target is a directory and the caller specified that it could be anything but a directory. '],
   3221225659: [
              'NtStatusNotSupported', 'The request is not supported. '],
   3221225660: [
              'NtStatusRemoteNotListening', 'This remote computer is not listening. '],
   3221225661: [
              'NtStatusDuplicateName', 'A duplicate name exists on the network. '],
   3221225662: [
              'NtStatusBadNetworkPath', 'The network path cannot be located. '],
   3221225663: [
              'NtStatusNetworkBusy', 'The network is busy. '],
   3221225675: [
              'NtErrorBadDeviceType', 'The specified device type (LPT, for example) conflicts with the actual device type on the remote resource. '],
   3221225676: [
              'NtErrorBadNetworkName', 'The specified share name cannot be found on the remote server. '],
   3221225689: [
              'NtErrorPipeEmpty', 'Used to indicate that a read operation was done on an empty pipe. '],
   3221225700: [
              'NtErrorCorruption', 'This error indicates that the requested operation cannot be completed due to a catastrophic media failure or on-disk data structure corruption. '],
   3221225704: [
              'NtErrorInvalidBuffer', 'An access to a user buffer failed at an "expected" point in time. This code is defined since the caller does not want to accept STATUS_ACCESS_VIOLATION in its filter. '],
   3221225760: [
              'NtErrorStatusCancelled', 'The I/O request was canceled. '],
   3221225803: [
              'NtErrorPipeBroken', 'The pipe operation has failed because the other end of the pipe has been closed. '],
   3221225813: [
              'NtErrorLogonNotGranted', 'A requested type of logon (e.g., Interactive, Network, Service) is not granted by the target systems local security policy. Please ask the system administrator to grant the necessary form of logon. '],
   3221225819: [
              'NtErrorLogonTypeNotGranted', 'A user has requested a type of logon (e.g., interactive or network) that has not been granted. An administrator has control over who may logon interactively and through the network. '],
   3221225825: [
              'NtErrorIllegalCharacter', 'An illegal character was encountered. For a multi-byte character set this includes a lead byte without a succeeding trail byte. For the Unicode character set this includes the characters 0xFFFF and 0xFFFE. '],
   3221225826: [
              'NtErrorUnmappableCharacter', 'No mapping for the Unicode character exists in the target multi-byte code page. '],
   3221225827: [
              'NtErrorUndefinedCharacter', 'The Unicode character is not defined in the Unicode character set installed on the system. '],
   3221225867: [
              'NtErrorNoTrustSamAccount', 'The SAM database on the Windows Server does not have a computer account for this workstation trust relationship. '],
   3221225989: [
              'NtErrorInsufficientServerResources', 'Insufficient server resources exist to complete the request.']
   }