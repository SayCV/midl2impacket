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
CONST_UNSIGNED_LONG = NDRULONG
UNSIGNED_HYPER = NDRUHYPER
HYPER = NDRHYPER

#################################################################################

#"ms-dtyp.idl"

#################################################################################

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

#lsarpc Definition

#################################################################################

MSRPC_UUID_LSARPC = uuidtup_to_bin(('12345778-1234-ABCD-EF00-0123456789AB','0.0'))

LSAPR_HANDLE = VOID
SECURITY_CONTEXT_TRACKING_MODE = UNSIGNED_CHAR
PSECURITY_CONTEXT_TRACKING_MODE = UNSIGNED_CHAR
SECURITY_DESCRIPTOR_CONTROL = UNSIGNED_SHORT
PSECURITY_DESCRIPTOR_CONTROL = UNSIGNED_SHORT

class DATA_STRING(NDRUniConformantArray):
    item = CHAR

class PTR_STRING(NDRPOINTER):
    referent = (
        ('Data', DATA_STRING),
    )

class STRING(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_SHORT),	('MaximumLength', UNSIGNED_SHORT),	('Buffer', PTR_STRING),

    )
        

class LSAPR_ACL(NDRSTRUCT):
    structure = (
        ('AclRevision', UNSIGNED_CHAR),('Sbz1', UNSIGNED_CHAR),('AclSize', UNSIGNED_SHORT),('Dummy1', UNSIGNED_CHAR),
    )
class PLSAPR_ACL(NDRPOINTER):
    referent = (
        ('Data', LSAPR_ACL),
    )    


class LSAPR_SECURITY_DESCRIPTOR(NDRSTRUCT):
    structure = (
        ('Revision', UNSIGNED_CHAR),('Sbz1', UNSIGNED_CHAR),('Control', SECURITY_DESCRIPTOR_CONTROL),('Owner', PRPC_SID),('Group', PRPC_SID),('Sacl', PLSAPR_ACL),('Dacl', PLSAPR_ACL),
    )
class PLSAPR_SECURITY_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', LSAPR_SECURITY_DESCRIPTOR),
    )    


SecurityAnonymous = 0,
SecurityIdentification = 1,
SecurityImpersonation = 2,
SecurityDelegation = 3
        

class SECURITY_QUALITY_OF_SERVICE(NDRSTRUCT):
    structure = (
        ('Length', UNSIGNED_LONG),('ImpersonationLevel', SECURITY_IMPERSONATION_LEVEL),('ContextTrackingMode', SECURITY_CONTEXT_TRACKING_MODE),('EffectiveOnly', UNSIGNED_CHAR),
    )
class PSECURITY_QUALITY_OF_SERVICE(NDRPOINTER):
    referent = (
        ('Data', SECURITY_QUALITY_OF_SERVICE),
    )    


class LSAPR_OBJECT_ATTRIBUTES(NDRSTRUCT):
    structure = (
        ('Length', UNSIGNED_LONG),('RootDirectory', UNSIGNED_CHAR),('ObjectName', PSTRING),('Attributes', UNSIGNED_LONG),('SecurityDescriptor', PLSAPR_SECURITY_DESCRIPTOR),('SecurityQualityOfService', PSECURITY_QUALITY_OF_SERVICE),
    )
class PLSAPR_OBJECT_ATTRIBUTES(NDRPOINTER):
    referent = (
        ('Data', LSAPR_OBJECT_ATTRIBUTES),
    )    


class LSAPR_TRUST_INFORMATION(NDRSTRUCT):
    structure = (
        ('Name', RPC_UNICODE_STRING),('Sid', PRPC_SID),
    )
class PLSAPR_TRUST_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUST_INFORMATION),
    )    


class LSAPR_REFERENCED_DOMAIN_LIST(NDRSTRUCT):
    structure = (
        ('Entries', UNSIGNED_LONG),('Domains', PLSAPR_TRUST_INFORMATION),('MaxEntries', UNSIGNED_LONG),
    )
class PLSAPR_REFERENCED_DOMAIN_LIST(NDRPOINTER):
    referent = (
        ('Data', LSAPR_REFERENCED_DOMAIN_LIST),
    )    


SidTypeUser = 1,
SidTypeGroup = 1,
SidTypeDomain = 1,
SidTypeAlias = 1,
SidTypeWellKnownGroup = 1,
SidTypeDeletedAccount = 1,
SidTypeInvalid = 1,
SidTypeUnknown = 1,
SidTypeComputer = 1
        

class LSA_TRANSLATED_SID(NDRSTRUCT):
    structure = (
        ('Use', SID_NAME_USE),('RelativeId', UNSIGNED_LONG),('DomainIndex', LONG),
    )
class PLSA_TRANSLATED_SID(NDRPOINTER):
    referent = (
        ('Data', LSA_TRANSLATED_SID),
    )    


class LSAPR_TRANSLATED_SIDS(NDRSTRUCT):
    structure = (
        ('Entries', UNSIGNED_LONG),('Sids', PLSA_TRANSLATED_SID),
    )
class PLSAPR_TRANSLATED_SIDS(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRANSLATED_SIDS),
    )    


LsapLookupWksta = 1,
LsapLookupPDC = 1,
LsapLookupTDL = 1,
LsapLookupGC = 1,
LsapLookupXForestReferral = 1,
LsapLookupXForestResolve = 1
        

class LSAPR_SID_INFORMATION(NDRSTRUCT):
    structure = (
        ('Sid', PRPC_SID),
    )
class PLSAPR_SID_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', LSAPR_SID_INFORMATION),
    )    


class LSAPR_SID_ENUM_BUFFER(NDRSTRUCT):
    structure = (
        ('Entries', UNSIGNED_LONG),('SidInfo', PLSAPR_SID_INFORMATION),
    )
class PLSAPR_SID_ENUM_BUFFER(NDRPOINTER):
    referent = (
        ('Data', LSAPR_SID_ENUM_BUFFER),
    )    


class LSAPR_TRANSLATED_NAME(NDRSTRUCT):
    structure = (
        ('Use', SID_NAME_USE),('Name', RPC_UNICODE_STRING),('DomainIndex', LONG),
    )
class PLSAPR_TRANSLATED_NAME(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRANSLATED_NAME),
    )    


class LSAPR_TRANSLATED_NAMES(NDRSTRUCT):
    structure = (
        ('Entries', UNSIGNED_LONG),('Names', PLSAPR_TRANSLATED_NAME),
    )
class PLSAPR_TRANSLATED_NAMES(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRANSLATED_NAMES),
    )    


class LSAPR_TRANSLATED_NAME_EX(NDRSTRUCT):
    structure = (
        ('Use', SID_NAME_USE),('Name', RPC_UNICODE_STRING),('DomainIndex', LONG),('Flags', UNSIGNED_LONG),
    )
class PLSAPR_TRANSLATED_NAME_EX(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRANSLATED_NAME_EX),
    )    


class LSAPR_TRANSLATED_NAMES_EX(NDRSTRUCT):
    structure = (
        ('Entries', UNSIGNED_LONG),('Names', PLSAPR_TRANSLATED_NAME_EX),
    )
class PLSAPR_TRANSLATED_NAMES_EX(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRANSLATED_NAMES_EX),
    )    


class LSAPR_TRANSLATED_SID_EX(NDRSTRUCT):
    structure = (
        ('Use', SID_NAME_USE),('RelativeId', UNSIGNED_LONG),('DomainIndex', LONG),('Flags', UNSIGNED_LONG),
    )
class PLSAPR_TRANSLATED_SID_EX(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRANSLATED_SID_EX),
    )    


class LSAPR_TRANSLATED_SIDS_EX(NDRSTRUCT):
    structure = (
        ('Entries', UNSIGNED_LONG),('Sids', PLSAPR_TRANSLATED_SID_EX),
    )
class PLSAPR_TRANSLATED_SIDS_EX(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRANSLATED_SIDS_EX),
    )    


class LSAPR_TRANSLATED_SID_EX2(NDRSTRUCT):
    structure = (
        ('Use', SID_NAME_USE),('Sid', PRPC_SID),('DomainIndex', LONG),('Flags', UNSIGNED_LONG),
    )
class PLSAPR_TRANSLATED_SID_EX2(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRANSLATED_SID_EX2),
    )    


class LSAPR_TRANSLATED_SIDS_EX2(NDRSTRUCT):
    structure = (
        ('Entries', UNSIGNED_LONG),('Sids', PLSAPR_TRANSLATED_SID_EX2),
    )
class PLSAPR_TRANSLATED_SIDS_EX2(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRANSLATED_SIDS_EX2),
    )    


class LsarClose(NDRCALL):
    opnum = 0
    structure = (
		('OBJECTHANDLE', LSAPR_HANDLE),
    )

class LsarCloseResponse(NDRCALL):
    structure = (
		('OBJECTHANDLE', LSAPR_HANDLE),
    )
        

class Opnum1NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum1NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_2(NDRCALL):
    opnum = 2
    structure = (

    )

class Lsar_LSA_DP_2Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_3(NDRCALL):
    opnum = 3
    structure = (

    )

class Lsar_LSA_DP_3Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_4(NDRCALL):
    opnum = 4
    structure = (

    )

class Lsar_LSA_DP_4Response(NDRCALL):
    structure = (

    )
        

class Opnum5NotUsedOnWire(NDRCALL):
    opnum = 5
    structure = (

    )

class Opnum5NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class LsarOpenPolicy(NDRCALL):
    opnum = 6
    structure = (
		('SYSTEMNAME', WCHAR_T),
		('OBJECTATTRIBUTES', PLSAPR_OBJECT_ATTRIBUTES),
		('DESIREDACCESS', ACCESS_MASK),
    )

class LsarOpenPolicyResponse(NDRCALL):
    structure = (
		('POLICYHANDLE', LSAPR_HANDLE),
    )
        

class Lsar_LSA_DP_7(NDRCALL):
    opnum = 7
    structure = (

    )

class Lsar_LSA_DP_7Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_8(NDRCALL):
    opnum = 8
    structure = (

    )

class Lsar_LSA_DP_8Response(NDRCALL):
    structure = (

    )
        

class Opnum9NotUsedOnWire(NDRCALL):
    opnum = 9
    structure = (

    )

class Opnum9NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_10(NDRCALL):
    opnum = 10
    structure = (

    )

class Lsar_LSA_DP_10Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_11(NDRCALL):
    opnum = 11
    structure = (

    )

class Lsar_LSA_DP_11Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_12(NDRCALL):
    opnum = 12
    structure = (

    )

class Lsar_LSA_DP_12Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_13(NDRCALL):
    opnum = 13
    structure = (

    )

class Lsar_LSA_DP_13Response(NDRCALL):
    structure = (

    )
        

class LsarLookupNames(NDRCALL):
    opnum = 14
    structure = (
		('POLICYHANDLE', LSAPR_HANDLE),
		('COUNT', UNSIGNED_LONG),
		('NAMES', PRPC_UNICODE_STRING),
		('TRANSLATEDSIDS', PLSAPR_TRANSLATED_SIDS),
		('LOOKUPLEVEL', LSAP_LOOKUP_LEVEL),
		('MAPPEDCOUNT', UNSIGNED_LONG),
    )

class LsarLookupNamesResponse(NDRCALL):
    structure = (
		('REFERENCEDDOMAINS', PLSAPR_REFERENCED_DOMAIN_LIST),
		('TRANSLATEDSIDS', PLSAPR_TRANSLATED_SIDS),
		('MAPPEDCOUNT', UNSIGNED_LONG),
    )
        

class LsarLookupSids(NDRCALL):
    opnum = 15
    structure = (
		('POLICYHANDLE', LSAPR_HANDLE),
		('SIDENUMBUFFER', PLSAPR_SID_ENUM_BUFFER),
		('TRANSLATEDNAMES', PLSAPR_TRANSLATED_NAMES),
		('LOOKUPLEVEL', LSAP_LOOKUP_LEVEL),
		('MAPPEDCOUNT', UNSIGNED_LONG),
    )

class LsarLookupSidsResponse(NDRCALL):
    structure = (
		('REFERENCEDDOMAINS', PLSAPR_REFERENCED_DOMAIN_LIST),
		('TRANSLATEDNAMES', PLSAPR_TRANSLATED_NAMES),
		('MAPPEDCOUNT', UNSIGNED_LONG),
    )
        

class Lsar_LSA_DP_16(NDRCALL):
    opnum = 16
    structure = (

    )

class Lsar_LSA_DP_16Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_17(NDRCALL):
    opnum = 17
    structure = (

    )

class Lsar_LSA_DP_17Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_18(NDRCALL):
    opnum = 18
    structure = (

    )

class Lsar_LSA_DP_18Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_19(NDRCALL):
    opnum = 19
    structure = (

    )

class Lsar_LSA_DP_19Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_20(NDRCALL):
    opnum = 20
    structure = (

    )

class Lsar_LSA_DP_20Response(NDRCALL):
    structure = (

    )
        

class Opnum21NotUsedOnWire(NDRCALL):
    opnum = 21
    structure = (

    )

class Opnum21NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum22NotUsedOnWire(NDRCALL):
    opnum = 22
    structure = (

    )

class Opnum22NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_23(NDRCALL):
    opnum = 23
    structure = (

    )

class Lsar_LSA_DP_23Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_24(NDRCALL):
    opnum = 24
    structure = (

    )

class Lsar_LSA_DP_24Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_25(NDRCALL):
    opnum = 25
    structure = (

    )

class Lsar_LSA_DP_25Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_26(NDRCALL):
    opnum = 26
    structure = (

    )

class Lsar_LSA_DP_26Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_27(NDRCALL):
    opnum = 27
    structure = (

    )

class Lsar_LSA_DP_27Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_28(NDRCALL):
    opnum = 28
    structure = (

    )

class Lsar_LSA_DP_28Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_29(NDRCALL):
    opnum = 29
    structure = (

    )

class Lsar_LSA_DP_29Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_30(NDRCALL):
    opnum = 30
    structure = (

    )

class Lsar_LSA_DP_30Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_31(NDRCALL):
    opnum = 31
    structure = (

    )

class Lsar_LSA_DP_31Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_32(NDRCALL):
    opnum = 32
    structure = (

    )

class Lsar_LSA_DP_32Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_33(NDRCALL):
    opnum = 33
    structure = (

    )

class Lsar_LSA_DP_33Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_34(NDRCALL):
    opnum = 34
    structure = (

    )

class Lsar_LSA_DP_34Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_35(NDRCALL):
    opnum = 35
    structure = (

    )

class Lsar_LSA_DP_35Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_36(NDRCALL):
    opnum = 36
    structure = (

    )

class Lsar_LSA_DP_36Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_37(NDRCALL):
    opnum = 37
    structure = (

    )

class Lsar_LSA_DP_37Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_38(NDRCALL):
    opnum = 38
    structure = (

    )

class Lsar_LSA_DP_38Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_39(NDRCALL):
    opnum = 39
    structure = (

    )

class Lsar_LSA_DP_39Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_40(NDRCALL):
    opnum = 40
    structure = (

    )

class Lsar_LSA_DP_40Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_41(NDRCALL):
    opnum = 41
    structure = (

    )

class Lsar_LSA_DP_41Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_42(NDRCALL):
    opnum = 42
    structure = (

    )

class Lsar_LSA_DP_42Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_43(NDRCALL):
    opnum = 43
    structure = (

    )

class Lsar_LSA_DP_43Response(NDRCALL):
    structure = (

    )
        

class LsarOpenPolicy2(NDRCALL):
    opnum = 44
    structure = (
		('SYSTEMNAME', WCHAR_T),
		('OBJECTATTRIBUTES', PLSAPR_OBJECT_ATTRIBUTES),
		('DESIREDACCESS', ACCESS_MASK),
    )

class LsarOpenPolicy2Response(NDRCALL):
    structure = (
		('POLICYHANDLE', LSAPR_HANDLE),
    )
        

class LsarGetUserName(NDRCALL):
    opnum = 45
    structure = (
		('SYSTEMNAME', WCHAR_T),
		('USERNAME', PRPC_UNICODE_STRING),
		('DOMAINNAME', PRPC_UNICODE_STRING),
    )

class LsarGetUserNameResponse(NDRCALL):
    structure = (
		('USERNAME', PRPC_UNICODE_STRING),
		('DOMAINNAME', PRPC_UNICODE_STRING),
    )
        

class Lsar_LSA_DP_46(NDRCALL):
    opnum = 46
    structure = (

    )

class Lsar_LSA_DP_46Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_47(NDRCALL):
    opnum = 47
    structure = (

    )

class Lsar_LSA_DP_47Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_48(NDRCALL):
    opnum = 48
    structure = (

    )

class Lsar_LSA_DP_48Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_49(NDRCALL):
    opnum = 49
    structure = (

    )

class Lsar_LSA_DP_49Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_50(NDRCALL):
    opnum = 50
    structure = (

    )

class Lsar_LSA_DP_50Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_51(NDRCALL):
    opnum = 51
    structure = (

    )

class Lsar_LSA_DP_51Response(NDRCALL):
    structure = (

    )
        

class Opnum52NotUsedOnWire(NDRCALL):
    opnum = 52
    structure = (

    )

class Opnum52NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_53(NDRCALL):
    opnum = 53
    structure = (

    )

class Lsar_LSA_DP_53Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_54(NDRCALL):
    opnum = 54
    structure = (

    )

class Lsar_LSA_DP_54Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_55(NDRCALL):
    opnum = 55
    structure = (

    )

class Lsar_LSA_DP_55Response(NDRCALL):
    structure = (

    )
        

class Opnum56NotUsedOnWire(NDRCALL):
    opnum = 56
    structure = (

    )

class Opnum56NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class LsarLookupSids2(NDRCALL):
    opnum = 57
    structure = (
		('POLICYHANDLE', LSAPR_HANDLE),
		('SIDENUMBUFFER', PLSAPR_SID_ENUM_BUFFER),
		('TRANSLATEDNAMES', PLSAPR_TRANSLATED_NAMES_EX),
		('LOOKUPLEVEL', LSAP_LOOKUP_LEVEL),
		('MAPPEDCOUNT', UNSIGNED_LONG),
		('LOOKUPOPTIONS', UNSIGNED_LONG),
		('CLIENTREVISION', UNSIGNED_LONG),
    )

class LsarLookupSids2Response(NDRCALL):
    structure = (
		('REFERENCEDDOMAINS', PLSAPR_REFERENCED_DOMAIN_LIST),
		('TRANSLATEDNAMES', PLSAPR_TRANSLATED_NAMES_EX),
		('MAPPEDCOUNT', UNSIGNED_LONG),
    )
        

class LsarLookupNames2(NDRCALL):
    opnum = 58
    structure = (
		('POLICYHANDLE', LSAPR_HANDLE),
		('COUNT', UNSIGNED_LONG),
		('NAMES', PRPC_UNICODE_STRING),
		('TRANSLATEDSIDS', PLSAPR_TRANSLATED_SIDS_EX),
		('LOOKUPLEVEL', LSAP_LOOKUP_LEVEL),
		('MAPPEDCOUNT', UNSIGNED_LONG),
		('LOOKUPOPTIONS', UNSIGNED_LONG),
		('CLIENTREVISION', UNSIGNED_LONG),
    )

class LsarLookupNames2Response(NDRCALL):
    structure = (
		('REFERENCEDDOMAINS', PLSAPR_REFERENCED_DOMAIN_LIST),
		('TRANSLATEDSIDS', PLSAPR_TRANSLATED_SIDS_EX),
		('MAPPEDCOUNT', UNSIGNED_LONG),
    )
        

class Lsar_LSA_DP_59(NDRCALL):
    opnum = 59
    structure = (

    )

class Lsar_LSA_DP_59Response(NDRCALL):
    structure = (

    )
        

class Opnum60NotUsedOnWire(NDRCALL):
    opnum = 60
    structure = (

    )

class Opnum60NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum61NotUsedOnWire(NDRCALL):
    opnum = 61
    structure = (

    )

class Opnum61NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum62NotUsedOnWire(NDRCALL):
    opnum = 62
    structure = (

    )

class Opnum62NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum63NotUsedOnWire(NDRCALL):
    opnum = 63
    structure = (

    )

class Opnum63NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum64NotUsedOnWire(NDRCALL):
    opnum = 64
    structure = (

    )

class Opnum64NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum65NotUsedOnWire(NDRCALL):
    opnum = 65
    structure = (

    )

class Opnum65NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum66NotUsedOnWire(NDRCALL):
    opnum = 66
    structure = (

    )

class Opnum66NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum67NotUsedOnWire(NDRCALL):
    opnum = 67
    structure = (

    )

class Opnum67NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class LsarLookupNames3(NDRCALL):
    opnum = 68
    structure = (
		('POLICYHANDLE', LSAPR_HANDLE),
		('COUNT', UNSIGNED_LONG),
		('NAMES', PRPC_UNICODE_STRING),
		('TRANSLATEDSIDS', PLSAPR_TRANSLATED_SIDS_EX2),
		('LOOKUPLEVEL', LSAP_LOOKUP_LEVEL),
		('MAPPEDCOUNT', UNSIGNED_LONG),
		('LOOKUPOPTIONS', UNSIGNED_LONG),
		('CLIENTREVISION', UNSIGNED_LONG),
    )

class LsarLookupNames3Response(NDRCALL):
    structure = (
		('REFERENCEDDOMAINS', PLSAPR_REFERENCED_DOMAIN_LIST),
		('TRANSLATEDSIDS', PLSAPR_TRANSLATED_SIDS_EX2),
		('MAPPEDCOUNT', UNSIGNED_LONG),
    )
        

class Opnum69NotUsedOnWire(NDRCALL):
    opnum = 69
    structure = (

    )

class Opnum69NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum70NotUsedOnWire(NDRCALL):
    opnum = 70
    structure = (

    )

class Opnum70NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum71NotUsedOnWire(NDRCALL):
    opnum = 71
    structure = (

    )

class Opnum71NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum72NotUsedOnWire(NDRCALL):
    opnum = 72
    structure = (

    )

class Opnum72NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_73(NDRCALL):
    opnum = 73
    structure = (

    )

class Lsar_LSA_DP_73Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_DP_74(NDRCALL):
    opnum = 74
    structure = (

    )

class Lsar_LSA_DP_74Response(NDRCALL):
    structure = (

    )
        

class Opnum75NotUsedOnWire(NDRCALL):
    opnum = 75
    structure = (

    )

class Opnum75NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class LsarLookupSids3(NDRCALL):
    opnum = 76
    structure = (
		('RPCHANDLE', HANDLE_T),
		('SIDENUMBUFFER', PLSAPR_SID_ENUM_BUFFER),
		('TRANSLATEDNAMES', PLSAPR_TRANSLATED_NAMES_EX),
		('LOOKUPLEVEL', LSAP_LOOKUP_LEVEL),
		('MAPPEDCOUNT', UNSIGNED_LONG),
		('LOOKUPOPTIONS', UNSIGNED_LONG),
		('CLIENTREVISION', UNSIGNED_LONG),
    )

class LsarLookupSids3Response(NDRCALL):
    structure = (
		('REFERENCEDDOMAINS', PLSAPR_REFERENCED_DOMAIN_LIST),
		('TRANSLATEDNAMES', PLSAPR_TRANSLATED_NAMES_EX),
		('MAPPEDCOUNT', UNSIGNED_LONG),
    )
        

class LsarLookupNames4(NDRCALL):
    opnum = 77
    structure = (
		('RPCHANDLE', HANDLE_T),
		('COUNT', UNSIGNED_LONG),
		('NAMES', PRPC_UNICODE_STRING),
		('TRANSLATEDSIDS', PLSAPR_TRANSLATED_SIDS_EX2),
		('LOOKUPLEVEL', LSAP_LOOKUP_LEVEL),
		('MAPPEDCOUNT', UNSIGNED_LONG),
		('LOOKUPOPTIONS', UNSIGNED_LONG),
		('CLIENTREVISION', UNSIGNED_LONG),
    )

class LsarLookupNames4Response(NDRCALL):
    structure = (
		('REFERENCEDDOMAINS', PLSAPR_REFERENCED_DOMAIN_LIST),
		('TRANSLATEDSIDS', PLSAPR_TRANSLATED_SIDS_EX2),
		('MAPPEDCOUNT', UNSIGNED_LONG),
    )
        
OPNUMS = {
0 : (LsarClose,LsarCloseResponse),
1 : (Opnum1NotUsedOnWire,Opnum1NotUsedOnWireResponse),
2 : (Lsar_LSA_DP_2,Lsar_LSA_DP_2Response),
3 : (Lsar_LSA_DP_3,Lsar_LSA_DP_3Response),
4 : (Lsar_LSA_DP_4,Lsar_LSA_DP_4Response),
5 : (Opnum5NotUsedOnWire,Opnum5NotUsedOnWireResponse),
6 : (LsarOpenPolicy,LsarOpenPolicyResponse),
7 : (Lsar_LSA_DP_7,Lsar_LSA_DP_7Response),
8 : (Lsar_LSA_DP_8,Lsar_LSA_DP_8Response),
9 : (Opnum9NotUsedOnWire,Opnum9NotUsedOnWireResponse),
10 : (Lsar_LSA_DP_10,Lsar_LSA_DP_10Response),
11 : (Lsar_LSA_DP_11,Lsar_LSA_DP_11Response),
12 : (Lsar_LSA_DP_12,Lsar_LSA_DP_12Response),
13 : (Lsar_LSA_DP_13,Lsar_LSA_DP_13Response),
14 : (LsarLookupNames,LsarLookupNamesResponse),
15 : (LsarLookupSids,LsarLookupSidsResponse),
16 : (Lsar_LSA_DP_16,Lsar_LSA_DP_16Response),
17 : (Lsar_LSA_DP_17,Lsar_LSA_DP_17Response),
18 : (Lsar_LSA_DP_18,Lsar_LSA_DP_18Response),
19 : (Lsar_LSA_DP_19,Lsar_LSA_DP_19Response),
20 : (Lsar_LSA_DP_20,Lsar_LSA_DP_20Response),
21 : (Opnum21NotUsedOnWire,Opnum21NotUsedOnWireResponse),
22 : (Opnum22NotUsedOnWire,Opnum22NotUsedOnWireResponse),
23 : (Lsar_LSA_DP_23,Lsar_LSA_DP_23Response),
24 : (Lsar_LSA_DP_24,Lsar_LSA_DP_24Response),
25 : (Lsar_LSA_DP_25,Lsar_LSA_DP_25Response),
26 : (Lsar_LSA_DP_26,Lsar_LSA_DP_26Response),
27 : (Lsar_LSA_DP_27,Lsar_LSA_DP_27Response),
28 : (Lsar_LSA_DP_28,Lsar_LSA_DP_28Response),
29 : (Lsar_LSA_DP_29,Lsar_LSA_DP_29Response),
30 : (Lsar_LSA_DP_30,Lsar_LSA_DP_30Response),
31 : (Lsar_LSA_DP_31,Lsar_LSA_DP_31Response),
32 : (Lsar_LSA_DP_32,Lsar_LSA_DP_32Response),
33 : (Lsar_LSA_DP_33,Lsar_LSA_DP_33Response),
34 : (Lsar_LSA_DP_34,Lsar_LSA_DP_34Response),
35 : (Lsar_LSA_DP_35,Lsar_LSA_DP_35Response),
36 : (Lsar_LSA_DP_36,Lsar_LSA_DP_36Response),
37 : (Lsar_LSA_DP_37,Lsar_LSA_DP_37Response),
38 : (Lsar_LSA_DP_38,Lsar_LSA_DP_38Response),
39 : (Lsar_LSA_DP_39,Lsar_LSA_DP_39Response),
40 : (Lsar_LSA_DP_40,Lsar_LSA_DP_40Response),
41 : (Lsar_LSA_DP_41,Lsar_LSA_DP_41Response),
42 : (Lsar_LSA_DP_42,Lsar_LSA_DP_42Response),
43 : (Lsar_LSA_DP_43,Lsar_LSA_DP_43Response),
44 : (LsarOpenPolicy2,LsarOpenPolicy2Response),
45 : (LsarGetUserName,LsarGetUserNameResponse),
46 : (Lsar_LSA_DP_46,Lsar_LSA_DP_46Response),
47 : (Lsar_LSA_DP_47,Lsar_LSA_DP_47Response),
48 : (Lsar_LSA_DP_48,Lsar_LSA_DP_48Response),
49 : (Lsar_LSA_DP_49,Lsar_LSA_DP_49Response),
50 : (Lsar_LSA_DP_50,Lsar_LSA_DP_50Response),
51 : (Lsar_LSA_DP_51,Lsar_LSA_DP_51Response),
52 : (Opnum52NotUsedOnWire,Opnum52NotUsedOnWireResponse),
53 : (Lsar_LSA_DP_53,Lsar_LSA_DP_53Response),
54 : (Lsar_LSA_DP_54,Lsar_LSA_DP_54Response),
55 : (Lsar_LSA_DP_55,Lsar_LSA_DP_55Response),
56 : (Opnum56NotUsedOnWire,Opnum56NotUsedOnWireResponse),
57 : (LsarLookupSids2,LsarLookupSids2Response),
58 : (LsarLookupNames2,LsarLookupNames2Response),
59 : (Lsar_LSA_DP_59,Lsar_LSA_DP_59Response),
60 : (Opnum60NotUsedOnWire,Opnum60NotUsedOnWireResponse),
61 : (Opnum61NotUsedOnWire,Opnum61NotUsedOnWireResponse),
62 : (Opnum62NotUsedOnWire,Opnum62NotUsedOnWireResponse),
63 : (Opnum63NotUsedOnWire,Opnum63NotUsedOnWireResponse),
64 : (Opnum64NotUsedOnWire,Opnum64NotUsedOnWireResponse),
65 : (Opnum65NotUsedOnWire,Opnum65NotUsedOnWireResponse),
66 : (Opnum66NotUsedOnWire,Opnum66NotUsedOnWireResponse),
67 : (Opnum67NotUsedOnWire,Opnum67NotUsedOnWireResponse),
68 : (LsarLookupNames3,LsarLookupNames3Response),
69 : (Opnum69NotUsedOnWire,Opnum69NotUsedOnWireResponse),
70 : (Opnum70NotUsedOnWire,Opnum70NotUsedOnWireResponse),
71 : (Opnum71NotUsedOnWire,Opnum71NotUsedOnWireResponse),
72 : (Opnum72NotUsedOnWire,Opnum72NotUsedOnWireResponse),
73 : (Lsar_LSA_DP_73,Lsar_LSA_DP_73Response),
74 : (Lsar_LSA_DP_74,Lsar_LSA_DP_74Response),
75 : (Opnum75NotUsedOnWire,Opnum75NotUsedOnWireResponse),
76 : (LsarLookupSids3,LsarLookupSids3Response),
77 : (LsarLookupNames4,LsarLookupNames4Response),
}
