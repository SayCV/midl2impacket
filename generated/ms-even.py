"""
Generated from MIDL2Impacket.py
"""


from __future__ import division
from __future__ import print_function
from impacket.dcerpc.v5.ndr import *
from impacket.dcerpc.v5.dtypes import *
from impacket.dcerpc.v5.lsad import PRPC_UNICODE_STRING_ARRAY
from impacket.structure import Structure
from impacket import nt_errors
from impacket.uuid import uuidtup_to_bin
from impacket.dcerpc.v5.rpcrt import DCERPCException

DWORD64 = NDRUHYPER
__INT64 = NDRHYPER
class CONTEXT_HANDLE(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )
HANDLE_T = CONTEXT_HANDLE
class RPC_STRING(NDRSTRUCT):
    structure = (
        ('Length','<H=0'),
        ('MaximumLength','<H=0'),
        ('Data',LPSTR),
    )

    def __setitem__(self, key, value):
        if key == 'Data' and isinstance(value, NDR) is False:
            self['Length'] = len(value)
            self['MaximumLength'] = len(value)
        return NDRSTRUCT.__setitem__(self, key, value)

    def dump(self, msg = None, indent = 0):
        if msg is None: msg = self.__class__.__name__
        if msg != '':
            print("%s" % msg, end=' ')

        if isinstance(self.fields['Data'] , NDRPOINTERNULL):
            print(" NULL", end=' ')
        elif self.fields['Data']['ReferentID'] == 0:
            print(" NULL", end=' ')
        else:
            return self.fields['Data'].dump('',indent)

class PRPC_STRING(NDRPOINTER):
    referent = (
        ('Data', RPC_STRING),
    )

UNSIGNED_SHORT = NDRUSHORT
UNSIGNED_CHAR = NDRCHAR
UNSIGNED_LONG = NDRULONG
UNSIGNED_INT = NDRULONG
UNSIGNED___INT64 = NDRUHYPER
SIGNED___INT64 = NDRHYPER
SIGNED_INT = NDRSHORT
SIGNED_LONG = NDRLONG
SIGNED_CHAR = NDRCHAR
SIGNED_SHORT = NDRSHORT
CONST_WCHAR_T = WSTR
CONST_CHAR = NDRCHAR
CONST_INT = NDRLONG
CONST_VOID = CONTEXT_HANDLE
CONST_LONG = NDRLONG
VOID = CONTEXT_HANDLE
__INT3264 = NDRLONG
UNSIGNED___INT3264 = NDRULONG

"""
Generated from MIDL2Impacket.py
"""


from __future__ import division
from __future__ import print_function
from impacket.dcerpc.v5.ndr import *
from impacket.dcerpc.v5.dtypes import *
from impacket.dcerpc.v5.lsad import PRPC_UNICODE_STRING_ARRAY
from impacket.structure import Structure
from impacket import nt_errors
from impacket.uuid import uuidtup_to_bin
from impacket.dcerpc.v5.rpcrt import DCERPCException

DWORD64 = NDRUHYPER
__INT64 = NDRHYPER
class CONTEXT_HANDLE(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )
HANDLE_T = CONTEXT_HANDLE
class RPC_STRING(NDRSTRUCT):
    structure = (
        ('Length','<H=0'),
        ('MaximumLength','<H=0'),
        ('Data',LPSTR),
    )

    def __setitem__(self, key, value):
        if key == 'Data' and isinstance(value, NDR) is False:
            self['Length'] = len(value)
            self['MaximumLength'] = len(value)
        return NDRSTRUCT.__setitem__(self, key, value)

    def dump(self, msg = None, indent = 0):
        if msg is None: msg = self.__class__.__name__
        if msg != '':
            print("%s" % msg, end=' ')

        if isinstance(self.fields['Data'] , NDRPOINTERNULL):
            print(" NULL", end=' ')
        elif self.fields['Data']['ReferentID'] == 0:
            print(" NULL", end=' ')
        else:
            return self.fields['Data'].dump('',indent)

class PRPC_STRING(NDRPOINTER):
    referent = (
        ('Data', RPC_STRING),
    )

UNSIGNED_SHORT = NDRUSHORT
UNSIGNED_CHAR = NDRCHAR
UNSIGNED_LONG = NDRULONG
UNSIGNED_INT = NDRULONG
UNSIGNED___INT64 = NDRUHYPER
SIGNED___INT64 = NDRHYPER
SIGNED_INT = NDRSHORT
SIGNED_LONG = NDRLONG
SIGNED_CHAR = NDRCHAR
SIGNED_SHORT = NDRSHORT
CONST_WCHAR_T = WSTR
CONST_CHAR = NDRCHAR
CONST_INT = NDRLONG
CONST_VOID = CONTEXT_HANDLE
CONST_LONG = NDRLONG
VOID = CONTEXT_HANDLE
__INT3264 = NDRLONG
UNSIGNED___INT3264 = NDRULONG

#################################################################################

#TYPEDEFS

#################################################################################

WCHAR_T = UNSIGNED_SHORT
ADCONNECTION_HANDLE = VOID
BOOL = INT
PBOOL = INT
LPBOOL = INT
BYTE = UNSIGNED_CHAR
PBYTE = UNSIGNED_CHAR
LPBYTE = UNSIGNED_CHAR
BOOLEAN = BYTE
PBOOLEAN = BYTE
WCHAR = WCHAR_T
PWCHAR = WCHAR_T
BSTR = WCHAR
CHAR = CHAR
PCHAR = CHAR
DOUBLE = DOUBLE
DWORD = UNSIGNED_LONG
PDWORD = UNSIGNED_LONG
LPDWORD = UNSIGNED_LONG
DWORD32 = UNSIGNED_INT
DWORD64 = UNSIGNED___INT64
PDWORD64 = UNSIGNED___INT64
ULONGLONG = UNSIGNED___INT64
DWORDLONG = ULONGLONG
PDWORDLONG = ULONGLONG
ERROR_STATUS_T = UNSIGNED_LONG
FLOAT = FLOAT
UCHAR = UNSIGNED_CHAR
PUCHAR = UNSIGNED_CHAR
SHORT = SHORT
HANDLE = VOID
HCALL = DWORD
INT = INT
LPINT = INT
INT8 = SIGNED_CHAR
INT16 = SIGNED_SHORT
INT32 = SIGNED_INT
INT64 = SIGNED___INT64
LDAP_UDP_HANDLE = VOID
LMCSTR = CONST_WCHAR_T
LMSTR = WCHAR
LONG = LONG
PLONG = LONG
LPLONG = LONG
LONGLONG = SIGNED___INT64
HRESULT = LONG
LONG_PTR = __INT3264
ULONG_PTR = UNSIGNED___INT3264
LONG32 = SIGNED_INT
LONG64 = SIGNED___INT64
PLONG64 = SIGNED___INT64
LPCSTR = CONST_CHAR
LPCVOID = CONST_VOID
LPCWSTR = CONST_WCHAR_T
PSTR = CHAR
LPSTR = CHAR
LPWSTR = WCHAR_T
PWSTR = WCHAR_T
NET_API_STATUS = DWORD
NTSTATUS = LONG
PCONTEXT_HANDLE = VOID
PPCONTEXT_HANDLE = PCONTEXT_HANDLE
QWORD = UNSIGNED___INT64
RPC_BINDING_HANDLE = VOID
STRING = UCHAR
UINT = UNSIGNED_INT
UINT8 = UNSIGNED_CHAR
UINT16 = UNSIGNED_SHORT
UINT32 = UNSIGNED_INT
UINT64 = UNSIGNED___INT64
ULONG = UNSIGNED_LONG
PULONG = UNSIGNED_LONG
DWORD_PTR = ULONG_PTR
SIZE_T = ULONG_PTR
ULONG32 = UNSIGNED_INT
ULONG64 = UNSIGNED___INT64
UNICODE = WCHAR_T
USHORT = UNSIGNED_SHORT
VOID = VOID
PVOID = VOID
LPVOID = VOID
WORD = UNSIGNED_SHORT
PWORD = UNSIGNED_SHORT
LPWORD = UNSIGNED_SHORT

class FILETIME(NDRSTRUCT):
    structure = (
        ('dwLowDateTime', DWORD),('dwHighDateTime', DWORD),
    )
class PFILETIME(NDRPOINTER):
    referent = (
        ('Data', FILETIME),
    )    
class LPFILETIME(NDRPOINTER):
    referent = (
        ('Data', FILETIME),
    )    


class GUID(NDRSTRUCT):
    structure = (
        ('Data1', UNSIGNED_LONG),('Data2', UNSIGNED_SHORT),('Data3', UNSIGNED_SHORT),('Data4', BYTE),
    )
UUID = GUID
class PGUID(NDRPOINTER):
    referent = (
        ('Data', GUID),
    )    


class LARGE_INTEGER(NDRSTRUCT):
    structure = (
        ('QuadPart', SIGNED___INT64),
    )
class PLARGE_INTEGER(NDRPOINTER):
    referent = (
        ('Data', LARGE_INTEGER),
    )    


class EVENT_DESCRIPTOR(NDRSTRUCT):
    structure = (
        ('Id', USHORT),('Version', UCHAR),('Channel', UCHAR),('Level', UCHAR),('Opcode', UCHAR),('Task', USHORT),('Keyword', ULONGLONG),
    )
class PEVENT_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', EVENT_DESCRIPTOR),
    )    
class PCEVENT_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', EVENT_DESCRIPTOR),
    )    


class S0(NDRSTRUCT):
    structure = (
        ('KernelTime', ULONG),('UserTime', ULONG),
    )


class U0(NDRUNION):
    union = {
        1: ('s0',S0),2: ('ProcessorTime',ULONG64),
    }
        

class EVENT_HEADER(NDRSTRUCT):
    structure = (
        ('Size', USHORT),('HeaderType', USHORT),('Flags', USHORT),('EventProperty', USHORT),('ThreadId', ULONG),('ProcessId', ULONG),('TimeStamp', LARGE_INTEGER),('ProviderId', GUID),('EventDescriptor', EVENT_DESCRIPTOR),('u0', U0),('ActivityId', GUID),
    )
class PEVENT_HEADER(NDRPOINTER):
    referent = (
        ('Data', EVENT_HEADER),
    )    

LCID = DWORD

class LUID(NDRSTRUCT):
    structure = (
        ('LowPart', DWORD),('HighPart', LONG),
    )
class PLUID(NDRPOINTER):
    referent = (
        ('Data', LUID),
    )    


class MULTI_SZ(NDRSTRUCT):
    structure = (
        ('Value', WCHAR_T),('nChar', DWORD),
    )


class DATA_RPC_UNICODE_STRING(NDRUniConformantArray):
    item = WCHAR

class PTR_RPC_UNICODE_STRING(NDRPOINTER):
    referent = (
        ('Data', DATA_RPC_UNICODE_STRING),
    )

class RPC_UNICODE_STRING(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_SHORT),	('MaximumLength', UNSIGNED_SHORT),	('Buffer', PTR_RPC_UNICODE_STRING),

    )
        

class SERVER_INFO_100(NDRSTRUCT):
    structure = (
        ('sv100_platform_id', DWORD),('sv100_name', WCHAR_T),
    )
class PSERVER_INFO_100(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_100),
    )    
class LPSERVER_INFO_100(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_100),
    )    


class SERVER_INFO_101(NDRSTRUCT):
    structure = (
        ('sv101_platform_id', DWORD),('sv101_name', WCHAR_T),('sv101_version_major', DWORD),('sv101_version_minor', DWORD),('sv101_version_type', DWORD),('sv101_comment', WCHAR_T),
    )
class PSERVER_INFO_101(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_101),
    )    
class LPSERVER_INFO_101(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_101),
    )    


class SYSTEMTIME(NDRSTRUCT):
    structure = (
        ('wYear', WORD),('wMonth', WORD),('wDayOfWeek', WORD),('wDay', WORD),('wHour', WORD),('wMinute', WORD),('wSecond', WORD),('wMilliseconds', WORD),
    )
class PSYSTEMTIME(NDRPOINTER):
    referent = (
        ('Data', SYSTEMTIME),
    )    


class UINT128(NDRSTRUCT):
    structure = (
        ('lower', UINT64),('upper', UINT64),
    )
class PUINT128(NDRPOINTER):
    referent = (
        ('Data', UINT128),
    )    


class ULARGE_INTEGER(NDRSTRUCT):
    structure = (
        ('QuadPart', UNSIGNED___INT64),
    )
class PULARGE_INTEGER(NDRPOINTER):
    referent = (
        ('Data', ULARGE_INTEGER),
    )    


class RPC_SID_IDENTIFIER_AUTHORITY(NDRSTRUCT):
    structure = (
        ('Value', BYTE),
    )

ACCESS_MASK = DWORD
PACCESS_MASK = ACCESS_MASK

class OBJECT_TYPE_LIST(NDRSTRUCT):
    structure = (
        ('Level', WORD),('Remaining', ACCESS_MASK),('ObjectType', GUID),
    )
class POBJECT_TYPE_LIST(NDRPOINTER):
    referent = (
        ('Data', OBJECT_TYPE_LIST),
    )    


class ACE_HEADER(NDRSTRUCT):
    structure = (
        ('AceType', UCHAR),('AceFlags', UCHAR),('AceSize', USHORT),
    )
class PACE_HEADER(NDRPOINTER):
    referent = (
        ('Data', ACE_HEADER),
    )    


class SYSTEM_MANDATORY_LABEL_ACE(NDRSTRUCT):
    structure = (
        ('Header', ACE_HEADER),('Mask', ACCESS_MASK),('SidStart', DWORD),
    )
class PSYSTEM_MANDATORY_LABEL_ACE(NDRPOINTER):
    referent = (
        ('Data', SYSTEM_MANDATORY_LABEL_ACE),
    )    


class TOKEN_MANDATORY_POLICY(NDRSTRUCT):
    structure = (
        ('Policy', DWORD),
    )
class PTOKEN_MANDATORY_POLICY(NDRPOINTER):
    referent = (
        ('Data', TOKEN_MANDATORY_POLICY),
    )    


class MANDATORY_INFORMATION(NDRSTRUCT):
    structure = (
        ('AllowedAccess', ACCESS_MASK),('WriteAllowed', BOOLEAN),('ReadAllowed', BOOLEAN),('ExecuteAllowed', BOOLEAN),('MandatoryPolicy', TOKEN_MANDATORY_POLICY),
    )
class PMANDATORY_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', MANDATORY_INFORMATION),
    )    


class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRSTRUCT):
    structure = (
        ('Length', DWORD),('OctetString', BYTE),
    )
class PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRPOINTER):
    referent = (
        ('Data', CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE),
    )    


class VALUES(NDRUNION):
    union = {
        1: ('pInt64',PLONG64),2: ('pUint64',PDWORD64),3: ('ppString',PWSTR),4: ('pOctetString',PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE),
    }
        

class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRSTRUCT):
    structure = (
        ('Name', DWORD),('ValueType', WORD),('Reserved', WORD),('Flags', DWORD),('ValueCount', DWORD),('Values', VALUES),
    )
class PCLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRPOINTER):
    referent = (
        ('Data', CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1),
    )    

SECURITY_INFORMATION = DWORD
PSECURITY_INFORMATION = DWORD

class RPC_SID(NDRSTRUCT):
    structure = (
        ('Revision', UNSIGNED_CHAR),('SubAuthorityCount', UNSIGNED_CHAR),('IdentifierAuthority', RPC_SID_IDENTIFIER_AUTHORITY),('SubAuthority', UNSIGNED_LONG),
    )
class PRPC_SID(NDRPOINTER):
    referent = (
        ('Data', RPC_SID),
    )    
class PSID(NDRPOINTER):
    referent = (
        ('Data', RPC_SID),
    )    


class ACL(NDRSTRUCT):
    structure = (
        ('AclRevision', UNSIGNED_CHAR),('Sbz1', UNSIGNED_CHAR),('AclSize', UNSIGNED_SHORT),('AceCount', UNSIGNED_SHORT),('Sbz2', UNSIGNED_SHORT),
    )
class PACL(NDRPOINTER):
    referent = (
        ('Data', ACL),
    )    


class SECURITY_DESCRIPTOR(NDRSTRUCT):
    structure = (
        ('Revision', UCHAR),('Sbz1', UCHAR),('Control', USHORT),('Owner', PSID),('Group', PSID),('Sacl', PACL),('Dacl', PACL),
    )
class PSECURITY_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', SECURITY_DESCRIPTOR),
    )    

#################################################################################

#TYPEDEFS

#################################################################################

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#eventlog Definition

#################################################################################

MSRPC_UUID_EVENTLOG = uuidtup_to_bin(('82273FDC-E32A-18C3-3F78-827929DC23EA','0.0'))


class DATA_RPC_STRING(NDRUniConformantArray):
    item = CHAR

class PTR_RPC_STRING(NDRPOINTER):
    referent = (
        ('Data', DATA_RPC_STRING),
    )

class RPC_STRING(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_SHORT),	('MaximumLength', UNSIGNED_SHORT),	('Buffer', PTR_RPC_STRING),

    )
        

class RPC_CLIENT_ID(NDRSTRUCT):
    structure = (
        ('UniqueProcess', UNSIGNED_LONG),('UniqueThread', UNSIGNED_LONG),
    )
class PRPC_CLIENT_ID(NDRPOINTER):
    referent = (
        ('Data', RPC_CLIENT_ID),
    )    

EVENTLOG_HANDLE_W = WCHAR_T
EVENTLOG_HANDLE_A = CHAR
IELF_HANDLE = VOID
PIELF_HANDLE = VOID
RULONG = UNSIGNED_LONG

class ElfrClearELFW(NDRCALL):
    opnum = 0
    structure = (
		('LOGHANDLE', IELF_HANDLE),
		('BACKUPFILENAME', PRPC_UNICODE_STRING),
    )

class ElfrClearELFWResponse(NDRCALL):
    structure = (

    )
        

class ElfrBackupELFW(NDRCALL):
    opnum = 1
    structure = (
		('LOGHANDLE', IELF_HANDLE),
		('BACKUPFILENAME', PRPC_UNICODE_STRING),
    )

class ElfrBackupELFWResponse(NDRCALL):
    structure = (

    )
        

class ElfrCloseEL(NDRCALL):
    opnum = 2
    structure = (
		('LOGHANDLE', IELF_HANDLE),
    )

class ElfrCloseELResponse(NDRCALL):
    structure = (
		('LOGHANDLE', IELF_HANDLE),
    )
        

class ElfrDeregisterEventSource(NDRCALL):
    opnum = 3
    structure = (
		('LOGHANDLE', IELF_HANDLE),
    )

class ElfrDeregisterEventSourceResponse(NDRCALL):
    structure = (
		('LOGHANDLE', IELF_HANDLE),
    )
        

class ElfrNumberOfRecords(NDRCALL):
    opnum = 4
    structure = (
		('LOGHANDLE', IELF_HANDLE),
    )

class ElfrNumberOfRecordsResponse(NDRCALL):
    structure = (
		('NUMBEROFRECORDS', UNSIGNED_LONG),
    )
        

class ElfrOldestRecord(NDRCALL):
    opnum = 5
    structure = (
		('LOGHANDLE', IELF_HANDLE),
    )

class ElfrOldestRecordResponse(NDRCALL):
    structure = (
		('OLDESTRECORDNUMBER', UNSIGNED_LONG),
    )
        

class ElfrChangeNotify(NDRCALL):
    opnum = 6
    structure = (
		('LOGHANDLE', IELF_HANDLE),
		('CLIENTID', RPC_CLIENT_ID),
		('EVENT', ULONG),
    )

class ElfrChangeNotifyResponse(NDRCALL):
    structure = (

    )
        

class ElfrOpenELW(NDRCALL):
    opnum = 7
    structure = (
		('UNCSERVERNAME', EVENTLOG_HANDLE_W),
		('MODULENAME', PRPC_UNICODE_STRING),
		('REGMODULENAME', PRPC_UNICODE_STRING),
		('MAJORVERSION', UNSIGNED_LONG),
		('MINORVERSION', UNSIGNED_LONG),
    )

class ElfrOpenELWResponse(NDRCALL):
    structure = (
		('LOGHANDLE', IELF_HANDLE),
    )
        

class ElfrRegisterEventSourceW(NDRCALL):
    opnum = 8
    structure = (
		('UNCSERVERNAME', EVENTLOG_HANDLE_W),
		('MODULENAME', PRPC_UNICODE_STRING),
		('REGMODULENAME', PRPC_UNICODE_STRING),
		('MAJORVERSION', UNSIGNED_LONG),
		('MINORVERSION', UNSIGNED_LONG),
    )

class ElfrRegisterEventSourceWResponse(NDRCALL):
    structure = (
		('LOGHANDLE', IELF_HANDLE),
    )
        

class ElfrOpenBELW(NDRCALL):
    opnum = 9
    structure = (
		('UNCSERVERNAME', EVENTLOG_HANDLE_W),
		('BACKUPFILENAME', PRPC_UNICODE_STRING),
		('MAJORVERSION', UNSIGNED_LONG),
		('MINORVERSION', UNSIGNED_LONG),
    )

class ElfrOpenBELWResponse(NDRCALL):
    structure = (
		('LOGHANDLE', IELF_HANDLE),
    )
        

class ElfrReadELW(NDRCALL):
    opnum = 10
    structure = (
		('LOGHANDLE', IELF_HANDLE),
		('READFLAGS', UNSIGNED_LONG),
		('RECORDOFFSET', UNSIGNED_LONG),
		('NUMBEROFBYTESTOREAD', RULONG),
    )

class ElfrReadELWResponse(NDRCALL):
    structure = (
		('BUFFER', UNSIGNED_CHAR),
		('NUMBEROFBYTESREAD', UNSIGNED_LONG),
		('MINNUMBEROFBYTESNEEDED', UNSIGNED_LONG),
    )
        

class ElfrReportEventW(NDRCALL):
    opnum = 11
    structure = (
		('LOGHANDLE', IELF_HANDLE),
		('TIME', UNSIGNED_LONG),
		('EVENTTYPE', UNSIGNED_SHORT),
		('EVENTCATEGORY', UNSIGNED_SHORT),
		('EVENTID', UNSIGNED_LONG),
		('NUMSTRINGS', UNSIGNED_SHORT),
		('DATASIZE', UNSIGNED_LONG),
		('COMPUTERNAME', PRPC_UNICODE_STRING),
		('USERSID', PRPC_SID),
		('STRINGS', PRPC_UNICODE_STRING),
		('DATA', UNSIGNED_CHAR),
		('FLAGS', UNSIGNED_SHORT),
		('RECORDNUMBER', UNSIGNED_LONG),
		('TIMEWRITTEN', UNSIGNED_LONG),
    )

class ElfrReportEventWResponse(NDRCALL):
    structure = (
		('RECORDNUMBER', UNSIGNED_LONG),
		('TIMEWRITTEN', UNSIGNED_LONG),
    )
        

class ElfrClearELFA(NDRCALL):
    opnum = 12
    structure = (
		('LOGHANDLE', IELF_HANDLE),
		('BACKUPFILENAME', PRPC_STRING),
    )

class ElfrClearELFAResponse(NDRCALL):
    structure = (

    )
        

class ElfrBackupELFA(NDRCALL):
    opnum = 13
    structure = (
		('LOGHANDLE', IELF_HANDLE),
		('BACKUPFILENAME', PRPC_STRING),
    )

class ElfrBackupELFAResponse(NDRCALL):
    structure = (

    )
        

class ElfrOpenELA(NDRCALL):
    opnum = 14
    structure = (
		('UNCSERVERNAME', EVENTLOG_HANDLE_A),
		('MODULENAME', PRPC_STRING),
		('REGMODULENAME', PRPC_STRING),
		('MAJORVERSION', UNSIGNED_LONG),
		('MINORVERSION', UNSIGNED_LONG),
    )

class ElfrOpenELAResponse(NDRCALL):
    structure = (
		('LOGHANDLE', IELF_HANDLE),
    )
        

class ElfrRegisterEventSourceA(NDRCALL):
    opnum = 15
    structure = (
		('UNCSERVERNAME', EVENTLOG_HANDLE_A),
		('MODULENAME', PRPC_STRING),
		('REGMODULENAME', PRPC_STRING),
		('MAJORVERSION', UNSIGNED_LONG),
		('MINORVERSION', UNSIGNED_LONG),
    )

class ElfrRegisterEventSourceAResponse(NDRCALL):
    structure = (
		('LOGHANDLE', IELF_HANDLE),
    )
        

class ElfrOpenBELA(NDRCALL):
    opnum = 16
    structure = (
		('UNCSERVERNAME', EVENTLOG_HANDLE_A),
		('BACKUPFILENAME', PRPC_STRING),
		('MAJORVERSION', UNSIGNED_LONG),
		('MINORVERSION', UNSIGNED_LONG),
    )

class ElfrOpenBELAResponse(NDRCALL):
    structure = (
		('LOGHANDLE', IELF_HANDLE),
    )
        

class ElfrReadELA(NDRCALL):
    opnum = 17
    structure = (
		('LOGHANDLE', IELF_HANDLE),
		('READFLAGS', UNSIGNED_LONG),
		('RECORDOFFSET', UNSIGNED_LONG),
		('NUMBEROFBYTESTOREAD', RULONG),
    )

class ElfrReadELAResponse(NDRCALL):
    structure = (
		('BUFFER', UNSIGNED_CHAR),
		('NUMBEROFBYTESREAD', UNSIGNED_LONG),
		('MINNUMBEROFBYTESNEEDED', UNSIGNED_LONG),
    )
        
OPNUMS = {
0 : (ElfrClearELFW,ElfrClearELFWResponse),
1 : (ElfrBackupELFW,ElfrBackupELFWResponse),
2 : (ElfrCloseEL,ElfrCloseELResponse),
3 : (ElfrDeregisterEventSource,ElfrDeregisterEventSourceResponse),
4 : (ElfrNumberOfRecords,ElfrNumberOfRecordsResponse),
5 : (ElfrOldestRecord,ElfrOldestRecordResponse),
6 : (ElfrChangeNotify,ElfrChangeNotifyResponse),
7 : (ElfrOpenELW,ElfrOpenELWResponse),
8 : (ElfrRegisterEventSourceW,ElfrRegisterEventSourceWResponse),
9 : (ElfrOpenBELW,ElfrOpenBELWResponse),
10 : (ElfrReadELW,ElfrReadELWResponse),
11 : (ElfrReportEventW,ElfrReportEventWResponse),
12 : (ElfrClearELFA,ElfrClearELFAResponse),
13 : (ElfrBackupELFA,ElfrBackupELFAResponse),
14 : (ElfrOpenELA,ElfrOpenELAResponse),
15 : (ElfrRegisterEventSourceA,ElfrRegisterEventSourceAResponse),
16 : (ElfrOpenBELA,ElfrOpenBELAResponse),
17 : (ElfrReadELA,ElfrReadELAResponse),
}
