# uncompyle6 version 2.9.10
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: c:\Temp\build\ZIBE\context_mgr.py
# Compiled at: 2013-02-28 20:41:28
import sys
import os
import datetime
from ctypes import *
from zbutil import OrderedDict, arg_to_utf8
import zibe_errors
import exceptions
try:
    zibe = CDLL('zibe-debug.dll')
except:
    zibe = None

if zibe is None:
    try:
        zibe = CDLL('zibe.dll')
    except:
        raise

class WIN32Constants(object):
    FILE_ATTRIBUTE_READONLY = 1
    FILE_ATTRIBUTE_HIDDEN = 2
    FILE_ATTRIBUTE_SYSTEM = 4
    FILE_ATTRIBUTE_DIRECTORY = 16
    FILE_ATTRIBUTE_ARCHIVE = 32
    FILE_ATTRIBUTE_DEVICE = 64
    FILE_ATTRIBUTE_NORMAL = 128
    FILE_ATTRIBUTE_TEMPORARY = 256
    FILE_ATTRIBUTE_COMPRESSED = 2048
    FILE_ATTRIBUTE_ENCRYPTED = 16384


DEFAULT_STRING_SIZE = 260

class SystemTime(Structure):
    _fields_ = [
     (
      'year', c_ushort),
     (
      'month', c_ushort),
     (
      'dayOfWeek', c_ushort),
     (
      'day', c_ushort),
     (
      'hour', c_ushort),
     (
      'minute', c_ushort),
     (
      'second', c_ushort),
     (
      'milliseconds', c_ushort)]


class FileInfo(Structure):
    _fields_ = [
     (
      'filename', c_char * DEFAULT_STRING_SIZE),
     (
      'attributes', c_uint),
     (
      'creation_time', SystemTime),
     (
      'last_access_time', SystemTime),
     (
      'last_write_time', SystemTime),
     (
      'filesize', c_longlong)]


class ZBServiceStatus(Structure):
    _fields_ = [
     (
      'service_type', c_ulong),
     (
      'current_state', c_ulong),
     (
      'controls_accepted', c_ulong),
     (
      'win32_exit_code', c_ulong),
     (
      'service_specific_exit_code', c_ulong),
     (
      'checkpoint', c_ulong),
     (
      'wait_hint', c_ulong),
     (
      'pid', c_ulong),
     (
      'service_flags', c_ulong)]


class ZBServiceStatusFull(Structure):
    _fields_ = [
     (
      'service_name', c_char * DEFAULT_STRING_SIZE),
     (
      'display_name', c_char * DEFAULT_STRING_SIZE),
     (
      'status', ZBServiceStatus)]


class RegistryValue(object):

    def __init__(self, name, type, value=None):
        self.name = name
        self.type = type
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return '[%s] type=%s, value=%s' % (self.name, self.type, str(self.value))


class RegMultiSZ(RegistryValue):

    def __init__(self, name, value=None):
        RegistryValue.__init__(self, name, 'REG_MULTI_SZ', value)

    def __str__(self):
        return ' '.join(self.value)

    def __repr__(self):
        return '[%s] %s %s' % (self.name, self.type, ' '.join(self.value))


class ZIBEException(Exception):

    def __init__(self, id):
        if id < 0:
            self.id = c_uint32(id).value
        else:
            self.id = id
        if zibe_errors.error_codes.has_key(self.id):
            error_data = zibe_errors.error_codes[self.id]
            self.message = error_data[1]
            self.name = error_data[0]
        else:
            self.message = 'Unknown error 0x%x' % self.id

    def __str__(self):
        return self.message + '\n'


class SCMException(ZIBEException):
    pass


class RegistryException(ZIBEException):
    pass


class ProcessException(ZIBEException):
    pass


class SAMException(ZIBEException):
    pass


class Context(object):
    PROVIDER_NTLM_PLAINTEXT = 49
    PROVIDER_NTLM_DOMAIN = 177
    PROVIDER_NTLM_HASH = 81
    PROVIDER_NTLM_DOMAIN_HASH = 209
    PROVIDER_KERB_PLAINTEXT = 818
    PROVIDER_KERB_HASH = 850
    PROVIDER_ESRO_PLAINTEXT = 819
    PROVIDER_ESRO_HASH = 851
    PROVIDER_DAPU = 1028

    def __init__(self, hCtx):
        self.hCtx = hCtx

    @property
    def localdir(self):
        return os.getcwd()

    def lcd(self, path):
        path = os.path.normpath(path)
        if not os.path.exists(path):
            raise exceptions.EnvironmentError("Path '%s' does not exist on the local system" % path)
        os.chdir(path)

    def close(self):
        pass

    def get_time_string(self, time):
        if time == 0:
            return '<not set>'
        intime = c_longlong(time)
        outstr = c_char_p(0)
        result = zibe.UTIL_FileTimeToString(byref(intime), byref(outstr))
        if result != 0:
            raise ZIBEException(result)
        ret = str(outstr.value)
        zibe.MEM_FreeBuffer(outstr)
        return ret

    def provider(self, value):
        result = zibe.CTX_SetAuthenticationProvider(self.hCtx, c_ulong(value))
        if result != 0:
            raise ZIBEException(result)

    def username(self, value):
        if '\\' in value:
            domain, name = value.split('\\')
        else:
            domain, name = None, value
        self.domain(domain)
        result = zibe.CTX_SetUsername(self.hCtx, c_char_p(name))
        if result != 0:
            raise ZIBEException(result)
        return

    def password(self, value):
        result = zibe.CTX_SetPassword(self.hCtx, c_char_p(value))
        if result != 0:
            raise ZIBEException(result)

    def password_hash(self, value):
        result = zibe.CTX_SetPasswordHash(self.hCtx, c_char_p(value))
        if result != 0:
            raise ZIBEException(result)

    def domain(self, value):
        if value:
            result = zibe.CTX_SetDomainName(self.hCtx, c_char_p(value), c_bool(False))
            if result != 0:
                raise ZIBEException(result)

    def kdc_location(self, target_ip, port, smb_port):
        result = zibe.CTX_SetKDCLocation(self.hCtx, c_char_p(target_ip), c_ushort(port), c_ushort(smb_port))
        if result != 0:
            raise ZIBEException(result)

    def target_name(self, value):
        result = zibe.CTX_SetTargetName(self.hCtx, c_char_p(value), c_uint(0))
        if result != 0:
            raise ZIBEException(result)

    def dp_key(self, value):
        result = zibe.CTX_SetDAPUKey(self.hCtx, c_char_p(value), c_uint(len(value)))
        if result != 0:
            raise ZIBEException(result)

    def start_session(self):
        result = zibe.CTX_StartSession(self.hCtx)
        if result != 0:
            raise ZIBEException(result)

    def finish_session(self):
        zibe.CTX_FinishSession(self.hCtx)

    def get_cwd(self):
        p = create_string_buffer(DEFAULT_STRING_SIZE)
        zibe.SMB_GetDirectory(self.hCtx, p, DEFAULT_STRING_SIZE)
        return str(p.value)

    def enumerate_shares(self):

        class ShareInfo(Structure):
            _fields_ = [
             (
              'share_name', c_char * DEFAULT_STRING_SIZE),
             (
              'remark', c_char * DEFAULT_STRING_SIZE),
             (
              'type', c_uint)]

        pshare = c_void_p(0)
        count = c_uint(0)
        result = zibe.SMB_EnumerateShares(self.hCtx, byref(pshare), byref(count))
        if result != 0:
            raise ZIBEException(result)
        count = count.value
        share_data = cast(pshare, POINTER(ShareInfo))
        ret = []
        for i in range(0, count):
            ret.append({'share_name': share_data[i].share_name,'remark': share_data[i].remark,
               'type': share_data[i].type
               })

        zibe.MEM_FreeBuffer(pshare)
        return ret

    def add_share(self, share_name, path):
        path = path.strip('\\')
        result = zibe.SMB_AddShare(self.hCtx, c_char_p(share_name), c_char_p(path))
        if result != 0:
            raise ZIBEException(result)

    def delete_share(self, share_name):
        result = zibe.SMB_DeleteShare(self.hCtx, c_char_p(share_name))
        if result != 0:
            raise ZIBEException(result)

    def use_share(self, share_name):
        result = zibe.SMB_UseShare(self.hCtx, c_char_p(share_name))
        if result != 0:
            raise ZIBEException(result)

    def change_directory(self, dir_name):
        result = zibe.SMB_ChangeDirectory(self.hCtx, c_char_p(dir_name))
        if result != 0:
            raise ZIBEException(result)

    def delete_file(self, filename):
        result = zibe.SMB_DeleteFile(self.hCtx, c_char_p(filename))
        if result != 0:
            raise ZIBEException(result)

    def create_directory(self, directory):
        result = zibe.SMB_CreateDirectory(self.hCtx, c_char_p(directory))
        if result != 0:
            raise ZIBEException(result)

    def remove_directory(self, directory):
        result = zibe.SMB_RemoveDirectory(self.hCtx, c_char_p(directory))
        if result != 0:
            raise ZIBEException(result)

    def _fileinfo_to_pydict(self, fi):
        try:
            creation_time = datetime.datetime(fi.creation_time.year, fi.creation_time.month, fi.creation_time.day, fi.creation_time.hour, fi.creation_time.minute, fi.creation_time.second, fi.creation_time.milliseconds)
        except ValueError:
            creation_time = '<error calculating>'

        try:
            last_access_time = datetime.datetime(fi.last_access_time.year, fi.last_access_time.month, fi.last_access_time.day, fi.last_access_time.hour, fi.last_access_time.minute, fi.last_access_time.second, fi.last_access_time.milliseconds)
        except:
            last_access_time = '<error calculating>'

        try:
            last_write_time = datetime.datetime(fi.last_write_time.year, fi.last_write_time.month, fi.last_write_time.day, fi.last_write_time.hour, fi.last_write_time.minute, fi.last_write_time.second, fi.last_write_time.milliseconds)
        except ValueError:
            last_write_time = '<error calculating>'

        return {'filename': fi.filename,'attributes': fi.attributes,'creation_time': creation_time,
           'last_access_time': last_access_time,'last_write_time': last_write_time,
           'filesize': fi.filesize}

    def get_file_details(self, filename):
        fi = FileInfo()
        result = zibe.SMB_GetFileDetails(self.hCtx, filename, byref(fi))
        if result != 0:
            raise ZIBEException(result)
        return self._fileinfo_to_pydict(fi)

    def dir_list(self, dir_name):
        plist = c_void_p(0)
        count = c_uint(0)
        result = zibe.SMB_DirList(self.hCtx, c_char_p(dir_name), byref(plist), byref(count))
        if result != 0:
            raise ZIBEException(result)
        count = count.value
        fi = cast(plist, POINTER(FileInfo))
        ret = []
        for i in range(0, count):
            ret.append(self._fileinfo_to_pydict(fi[i]))

        zibe.MEM_FreeBuffer(plist)
        return ret

    def put_file(self, filename, file_contents):
        result = zibe.SMB_PutFile(self.hCtx, filename, cast(file_contents, POINTER(c_byte)), c_uint(len(file_contents)))
        if result != 0:
            raise ZIBEException(result)

    def get_file(self, filename):
        file_contents = c_void_p(0)
        file_size = c_uint(0)
        result = zibe.SMB_GetFile(self.hCtx, c_char_p(filename), byref(file_contents), byref(file_size))
        if result != 0:
            raise ZIBEException(result)
        ret = cast(file_contents, POINTER(c_char))[:file_size.value]
        zibe.MEM_FreeBuffer(file_contents)
        return ret

    def get_version_strings(self):
        osString = c_char_p(0)
        lmString = c_char_p(0)
        result = zibe.SMB_GetNativeVersionStrings(self.hCtx, byref(osString), byref(lmString))
        if result != 0:
            raise ZIBEException(result)
        ret = [
         str(osString.value),
         str(lmString.value)]
        zibe.MEM_FreeBuffer(osString)
        zibe.MEM_FreeBuffer(lmString)
        return ret

    def _get_service_type(self, type):
        if type == 2:
            return 'FS Driver'
        if type == 1:
            return 'Driver'
        if type == 16:
            return 'Service'
        if type == 32:
            return 'Service (s)'
        return 'Unknown'

    def get_services(self):
        svc_list = c_void_p(0)
        count = c_uint(0)
        result = zibe.SCM_EnumServices(self.hCtx, byref(svc_list), byref(count))
        if result != 0:
            raise ZIBEException(result)
        count = count.value
        svc_data = cast(svc_list, POINTER(ZBServiceStatusFull))
        ret = []
        states = ('Unknown', 'Stopped', 'Pause Pending', 'Paused', 'Running', 'Start Pending',
                  'Stop Pending', 'Stopped')
        for i in range(0, count):
            ret.append({'service_name': svc_data[i].service_name,'display_name': svc_data[i].display_name,
               'svc_exit_code': svc_data[i].status.service_specific_exit_code,
               'type': self._get_service_type(svc_data[i].status.service_type),
               'state': states[svc_data[i].status.current_state],
               'pid': svc_data[i].status.pid,
               'service_flags': svc_data[i].status.service_flags,
               'win32_exit_code': svc_data[i].status.win32_exit_code
               })

        zibe.MEM_FreeBuffer(svc_data)
        return ret

    def query_service_config(self, service_name):

        class ZBServiceConfig(Structure):
            _fields_ = [
             (
              'service_type', c_ulong),
             (
              'start_type', c_ulong),
             (
              'error_control', c_ulong),
             (
              'binarypath_name', c_char * DEFAULT_STRING_SIZE),
             (
              'load_order_group', c_char * DEFAULT_STRING_SIZE),
             (
              'tag_id', c_ulong),
             (
              'dependencies', c_char * DEFAULT_STRING_SIZE),
             (
              'service_start_name', c_char * DEFAULT_STRING_SIZE),
             (
              'display_name', c_char * DEFAULT_STRING_SIZE)]

        config = ZBServiceConfig()
        result = zibe.SCM_QueryServiceConfig(self.hCtx, c_char_p(service_name), byref(config))
        if result != 0:
            raise ZIBEException(result)
        start_types = ('Boot Start', 'System Start', 'Auto Start', 'Demand Start',
                       'Disabled')
        return {'binarypath_name': config.binarypath_name,'load_order_group': config.load_order_group,
           'dependencies': config.dependencies,
           'service_start_name': config.service_start_name,
           'display_name': config.display_name,
           'type': self._get_service_type(config.service_type),
           'start_type': start_types[config.start_type]
           }

    def query_service_status(self, service_name):
        status = ZBServiceStatus()
        result = zibe.SCM_QueryServiceStatus(self.hCtx, c_char_p(service_name), byref(status))
        if result != 0:
            raise ZIBEException(result)
        states = ('Unknown', 'Stopped', 'Pause Pending', 'Paused', 'Running', 'Start Pending',
                  'Stop Pending', 'Stopped')
        return {'svc_exit_code': status.service_specific_exit_code,'type': self._get_service_type(status.service_type),
           'state': states[status.current_state],
           'pid': status.pid,
           'win32_exit_code': status.win32_exit_code
           }

    def start_service(self, service_name):
        result = zibe.SCM_StartService(self.hCtx, c_char_p(service_name))
        if result != 0:
            raise ZIBEException(result)

    def stop_service(self, service_name):
        result = zibe.SCM_StopService(self.hCtx, c_char_p(service_name))
        if result != 0:
            raise ZIBEException(result)

    def enumerate_jobs(self):

        class ZBJobEntry(Structure):
            _fields_ = [
             (
              'job_id', c_uint),
             (
              'job_time', c_uint),
             (
              'days_month', c_uint),
             (
              'days_week', c_uint),
             (
              'flags', c_uint),
             (
              'cmd', c_char * DEFAULT_STRING_SIZE)]

        job_list = c_void_p(0)
        count = c_uint(0)
        result = zibe.JOB_EnumerateJobs(self.hCtx, byref(job_list), byref(count))
        if result != 0:
            raise ZIBEException(result)
        jl = cast(job_list, POINTER(ZBJobEntry))
        count = count.value
        ret = []
        MILLISECONDS_IN_SECOND = 1000
        MILLISECONDS_IN_MINUTE = 60 * MILLISECONDS_IN_SECOND
        MILLISECONDS_IN_HOUR = 60 * MILLISECONDS_IN_MINUTE
        for i in range(0, count):
            job_time = int(jl[i].job_time)
            hour = job_time / MILLISECONDS_IN_HOUR
            minute = int((job_time - hour * MILLISECONDS_IN_HOUR) / MILLISECONDS_IN_MINUTE)
            secs = int((job_time - (hour * MILLISECONDS_IN_HOUR + minute * MILLISECONDS_IN_MINUTE)) / MILLISECONDS_IN_SECOND)
            time = '%.2d:%.2d:%.2d' % (hour, minute, secs)
            ret.append({'job_id': jl[i].job_id,'job_time': time,
               'days_month': jl[i].days_month,
               'flags': jl[i].flags,
               'cmd': jl[i].cmd
               })

        zibe.MEM_FreeBuffer(job_list)
        return ret

    def add_job_now(self, command):
        job_id = c_uint(0)
        result = zibe.JOB_AddJobNow(self.hCtx, c_char_p(command), byref(job_id))
        if result != 0:
            raise ZIBEException(result)
        return int(job_id.value)

    def add_job(self, command, hours_from_midnight, mins_from_hour):
        job_id = c_uint(0)
        result = zibe.JOB_AddJob(self.hCtx, c_char_p(command), c_uint(hours_from_midnight), c_uint(mins_from_hour), byref(job_id))
        if result != 0:
            raise ZIBEException(result)
        return int(job_id.value)

    def delete_job(self, job_id):
        result = zibe.JOB_DeleteJob(self.hCtx, c_uint(job_id))
        if result != 0:
            raise ZIBEException(result)

    def kill_process(self, pid):
        exit_code = c_uint(0)
        result = zibe.PROC_TerminateProcess(self.hCtx, c_uint(pid), c_uint(0), byref(exit_code))
        if result != 0:
            raise ZIBEException(result)
        return exit_code

    ENUM_PROC_BY_WINREG = 0
    ENUM_PROC_BY_TS = 1

    def enumerate_processes(self, enum_type):

        class ZSBProcessInfo(Structure):
            _fields_ = [
             (
              'pid', c_uint),
             (
              'ppid', c_uint),
             (
              'image_name', c_char * DEFAULT_STRING_SIZE),
             (
              'thread_count', c_uint),
             (
              'handle_count', c_uint),
             (
              'account_name', c_char * DEFAULT_STRING_SIZE)]

        count = c_uint(0)
        process_list = c_void_p(0)
        result = zibe.PROC_EnumProcesses(self.hCtx, enum_type, byref(count), byref(process_list))
        if result != 0:
            raise ZIBEException(result)
        count = count.value
        pi = cast(process_list, POINTER(ZSBProcessInfo))
        ret = []
        for i in range(0, count):
            ret.append({'pid': pi[i].pid,'ppid': pi[i].ppid,
               'image_name': pi[i].image_name,
               'thread_count': pi[i].thread_count,
               'handle_count': pi[i].handle_count,
               'account_name': pi[i].account_name
               })

        zibe.MEM_FreeBuffer(process_list)
        return ret

    REG_SZ = 1
    REG_EXPAND_SZ = 2
    REG_BINARY = 3
    REG_DWORD = 4
    REG_MULTI_SZ = 7
    REG_QWORD = 11

    def change_hive(self, hive_name):
        hive = 0
        hive_name = hive_name.lower()
        if hive_name == 'hklm':
            hive = 2
        else:
            if hive_name == 'hkcr':
                hive = 0
            elif hive_name == 'hku':
                hive = 4
            elif hive_name == 'hkcu':
                hive = 1
            else:
                raise Exception('Invalid hive name')
            result = zibe.REG_ChangeHive(self.hCtx, c_uint(hive))
            if result != 0:
                raise ZIBEException(result)

    def change_cwk(self, key_name):
        result = zibe.REG_ChangeCWK(self.hCtx, key_name)
        if result != 0:
            raise ZIBEException(result)

    def get_cwk(self):
        cwk = c_char_p(0)
        result = zibe.REG_GetCWK(self.hCtx, byref(cwk))
        if result != 0:
            raise ZIBEException(result)
        ret = str(cwk.value)
        zibe.MEM_FreeBuffer(cwk)
        return ret

    def create_key(self, key_name):
        result = zibe.REG_CreateKey(self.hCtx, key_name)
        if result != 0:
            raise ZIBEException(result)

    def delete_key(self, key_name):
        result = zibe.REG_DeleteKey(self.hCtx, key_name)
        if result != 0:
            raise ZIBEException(result)

    def delete_value(self, value_name):
        result = zibe.REG_DeleteValue(self.hCtx, value_name)
        if result != 0:
            raise ZIBEException(result)

    def set_reg_value(self, value_name, data_type, data):
        if type(data) == list:
            tmp_string = ''
            for s in data:
                tmp_string += s + '\x00'

            tmp_string += '\x00'
            m_data = create_string_buffer(tmp_string)
            m_len = len(tmp_string)
        else:
            if type(data) == str:
                m_data = c_char_p(data)
                m_len = len(data)
            elif type(data) == int:
                m_data = byref(c_uint(data))
                m_len = 4
            result = zibe.REG_SetValue(self.hCtx, value_name, m_data, c_uint(m_len), c_uint(data_type))
            if result != 0:
                raise ZIBEException(result)

    def get_reg_values(self, value_name):
        if value_name == '*':
            ret = []
            for v in self.enum_value_names():
                ret.append(self._do_get_reg_value(v))

            return ret
        return [
         self._do_get_reg_value(value_name)]

    def _convert_reg_result(self, value_data, value_type, value_size):
        ret = None
        type = ''
        if value_type == 1 or value_type == 2:
            if value_type == 1:
                type = 'REG_SZ'
            elif value_type == 2:
                type = 'REG_EXPAND_SZ'
            ret = cast(value_data, POINTER(c_char))[:value_size]
        elif value_type == 3:
            ret = cast(value_data, POINTER(c_char))[:value_size]
            type = 'REG_BINARY'
        elif value_type == 4:
            ret = int(cast(value_data, POINTER(c_uint))[0])
            type = 'REG_DWORD'
        elif value_type == 11:
            ret = int(cast(value_data, POINTER(c_ulonglong))[0])
            type = 'REG_QWORD'
        elif value_type == 7:
            type = 'REG_MULTI_SZ'
            ret = []
            ret = cast(value_data, POINTER(c_char))[:value_size]
        else:
            raise Exception('Unknown registry type')
        return (ret, type)

    def _do_get_reg_value(self, value_name):
        value_type = c_uint(0)
        value_size = c_uint(0)
        value_data = c_void_p(0)
        result = zibe.REG_GetValue(self.hCtx, value_name, byref(value_data), byref(value_size), byref(value_type))
        if result != 0:
            raise ZIBEException(result)
        value_size = value_size.value
        value_type = value_type.value
        ret, type = self._convert_reg_result(value_data, value_type, value_size)
        zibe.MEM_FreeBuffer(value_data)
        return (
         value_name, type, ret)

    def enum_values(self):

        class SizedBuffer(Structure):
            _fields_ = [
             (
              'buffer', c_void_p),
             (
              'size', c_size_t),
             (
              'allocated', c_size_t),
             (
              'flags', c_uint)]

        class ZBRegValue(Structure):
            _fields_ = [
             (
              'name', SizedBuffer),
             (
              'type', c_uint),
             (
              'value', SizedBuffer)]

        values = c_void_p(0)
        count = c_uint(0)
        result = zibe.REG_GetValues(self.hCtx, byref(values), byref(count))
        if result != 0:
            raise ZIBEException(result)
        ret = []
        valArray = cast(values, POINTER(ZBRegValue))
        for i in xrange(count.value):
            name = str(cast(valArray[i].name.buffer, c_char_p).value[:])
            type = int(valArray[i].type)
            value_data = valArray[i].value.buffer
            value_size = valArray[i].value.size
            data, strtype = self._convert_reg_result(value_data, type, value_size)
            ret.append({'name': name,'type': strtype,'data': data})

        zibe.MEM_FreeBuffer(values)
        return ret

    def enum_keys(self):
        subkeys = c_char_p(0)
        result = zibe.REG_GetSubKeys(self.hCtx, byref(subkeys))
        if result != 0:
            raise ZIBEException(result)
        data = cast(subkeys, POINTER(c_char))
        ret = self._multisz_to_list(data)
        zibe.MEM_FreeBuffer(data)
        return ret

    def enum_value_names(self):
        value_names = c_char_p(0)
        result = zibe.REG_GetValueNames(self.hCtx, byref(value_names))
        if result != 0:
            raise ZIBEException(result)
        ret = self._multisz_to_list(cast(value_names, POINTER(c_char)))
        zibe.MEM_FreeBuffer(value_names)
        return ret

    def _multisz_to_list(self, data):
        i = 0
        rv = []
        while data[i] != '\x00':
            rv.append(i)
            while data[i] != '\x00':
                i += 1

            i += 1

        rv.append(i)
        ret = []
        for i in range(len(rv) - 1):
            ret.append(data[rv[i]:rv[i + 1] - 1])

        return ret

    def add_tunnel(self, connect_ip_address, connect_port, listen_port):
        result = zibe.TUN_AddTunnel(self.hCtx, c_char_p(connect_ip_address), c_uint(connect_port), c_uint(listen_port))
        if result != 0:
            raise ZIBEException(result)

    def delete_tunnel(self, listen_port):
        result = zibe.TUN_DeleteTunnel(self.hCtx, c_uint(listen_port))
        if result != 0:
            raise ZIBEException(result)

    def enum_tunnels(self):

        class ZBTunnelRecord(Structure):
            _fields_ = [
             (
              'tunnel_type', c_uint),
             (
              'connect_ip_address', c_char * DEFAULT_STRING_SIZE),
             (
              'connect_port', c_ushort),
             (
              'listen_port', c_ushort)]

        count = c_uint(0)
        ptunnel = c_void_p(0)
        result = zibe.TUN_EnumRemoteTunnels(self.hCtx, byref(ptunnel), byref(count))
        if result != 0:
            raise ZIBEException(result)
        ti = cast(ptunnel, POINTER(ZBTunnelRecord))
        ret = []
        count = count.value
        for i in range(0, count):
            ret.append({'tunnel_type': ti[i].tunnel_type,'connect_ip_address': ti[i].connect_ip_address,
               'connect_port': ti[i].connect_port,
               'listen_port': ti[i].listen_port
               })

        zibe.MEM_FreeBuffer(ptunnel)
        return ret

    def enum_users(self):

        class ZBRemoteUserRecord(Structure):
            _fields_ = [
             (
              'rid', c_uint),
             (
              'account_name', c_char * DEFAULT_STRING_SIZE)]

        count = c_uint(0)
        precords = c_void_p(0)
        result = zibe.SAM_GetRemoteUserList(self.hCtx, byref(precords), byref(count))
        if result != 0:
            raise ZIBEException(result)
        recs = cast(precords, POINTER(ZBRemoteUserRecord))
        ret = []
        count = count.value
        for i in range(0, count):
            ret.append({'rid': int(recs[i].rid),'account_name': recs[i].account_name
               })

        zibe.MEM_FreeBuffer(precords)
        return ret

    def get_user_info_by_name(self, name):
        for user in self.enum_users():
            if user['account_name'].lower() == name.lower():
                return self.get_user_info_by_rid(user['rid'])
            if '\\' in user['account_name'] and user['account_name'].split('\\')[1].lower() == name.lower():
                return self.get_user_info_by_rid(user['rid'])

        raise ZIBEException(3221225572)

    def get_user_info_by_rid(self, rid):

        class ZBRemoteUserRecord(Structure):
            _fields_ = [
             (
              'UserName', c_char_p),
             (
              'FullName', c_char_p),
             (
              'UserId', c_uint),
             (
              'PrimaryGroupId', c_uint),
             (
              'HomeDirectory', c_char_p),
             (
              'HomeDirectoryDrive', c_char_p),
             (
              'ScriptPath', c_char_p),
             (
              'ProfilePath', c_char_p),
             (
              'WorkStations', c_char_p),
             (
              'LastLogon', c_longlong),
             (
              'LastLogoff', c_longlong),
             (
              'PasswordLastSet', c_longlong),
             (
              'PasswordCanChange', c_longlong),
             (
              'PasswordMustChange', c_longlong),
             (
              'BadPasswordCount', c_uint),
             (
              'LogonCount', c_uint),
             (
              'UserAccountControl', c_uint)]

        r = pointer(ZBRemoteUserRecord())
        result = zibe.SAM_GetRemoteUserInfoByRID(self.hCtx, c_uint(rid), byref(r))
        if result != 0:
            raise ZIBEException(result)
        ret = OrderedDict()
        ret['UserName'] = r[0].UserName
        ret['FullName'] = r[0].FullName
        ret['UserId'] = r[0].UserId
        ret['PrimaryGroupId'] = r[0].PrimaryGroupId
        ret['HomeDirectory'] = r[0].HomeDirectory
        ret['HomeDirectoryDrive'] = r[0].HomeDirectoryDrive
        ret['ScriptPath'] = r[0].ScriptPath
        ret['ProfilePath'] = r[0].ProfilePath
        ret['WorkStations'] = r[0].WorkStations
        ret['LastLogon'] = self.get_time_string(r[0].LastLogon)
        ret['LastLogoff'] = self.get_time_string(r[0].LastLogoff)
        ret['PasswordLastSet'] = self.get_time_string(r[0].PasswordLastSet)
        ret['PasswordCanChange'] = self.get_time_string(r[0].PasswordCanChange)
        ret['PasswordMustChange'] = self.get_time_string(r[0].PasswordMustChange)
        ret['BadPasswordCount'] = r[0].BadPasswordCount
        ret['LogonCount'] = r[0].LogonCount
        ret['UserAccountControl'] = r[0].UserAccountControl
        return ret

    SAM_ADD_USER_MAKE_ADMIN = 1

    def add_user(self, username, password, flags):
        result = zibe.SAM_AddUser(self.hCtx, c_char_p(username), c_char_p(password), c_uint(flags))
        if result != 0:
            raise ZIBEException(result)

    def delete_user(self, username):
        result = zibe.SAM_DeleteUser(self.hCtx, c_char_p(username))
        if result != 0:
            raise ZIBEException(result)


class ContextManager(object):

    def __init__(self):
        self.hCtxMgr = c_void_p(0)
        result = zibe.CM_GetContextManager(byref(self.hCtxMgr))
        if result is not 0:
            raise ZIBEException(result)

    def __del__(self):
        pass

    def create_context(self, context_name, target_address, smb_port, epm_port):
        hCtx = c_void_p(0)
        result = zibe.CM_CreateContext(self.hCtxMgr, c_char_p(context_name), c_char_p(target_address), c_ushort(smb_port), c_ushort(epm_port), byref(hCtx))
        if result is not 0:
            raise ZIBEException(result)
        return Context(hCtx)

    def release_context(self, ctx):
        zibe.CTX_ReleaseContext(ctx.hCtx)
        ctx.hCtx = None
        return