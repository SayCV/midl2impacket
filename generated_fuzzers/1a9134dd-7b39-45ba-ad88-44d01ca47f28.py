from fuzzer.midl import *
from fuzzer.core import *


class FILETIME(NdrStructure):
    MEMBERS = [
        (DWORD, "dwLowDateTime"),
        (DWORD, "dwHighDateTime"),
    ]


class GUID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "Data1"),
        (UNSIGNED_SHORT, "Data2"),
        (UNSIGNED_SHORT, "Data3"),
        (BYTE, "Data4"),
    ]


class LARGE_INTEGER(NdrStructure):
    MEMBERS = [
        (SIGNED___INT64, "QuadPart"),
    ]


class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [
        (USHORT, "Id"),
        (UCHAR, "Version"),
        (UCHAR, "Channel"),
        (UCHAR, "Level"),
        (UCHAR, "Opcode"),
        (USHORT, "Task"),
        (ULONGLONG, "Keyword"),
    ]


class S0(NdrStructure):
    MEMBERS = [
        (ULONG, "KernelTime"),
        (ULONG, "UserTime"),
    ]


class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (S0, "s0"),
        2: (ULONG64, "ProcessorTime"),
    }


class EVENT_HEADER(NdrStructure):
    MEMBERS = [
        (USHORT, "Size"),
        (USHORT, "HeaderType"),
        (USHORT, "Flags"),
        (USHORT, "EventProperty"),
        (ULONG, "ThreadId"),
        (ULONG, "ProcessId"),
        (LARGE_INTEGER, "TimeStamp"),
        (GUID, "ProviderId"),
        (EVENT_DESCRIPTOR, "EventDescriptor"),
        (U0, "u0"),
        (GUID, "ActivityId"),
    ]


class LUID(NdrStructure):
    MEMBERS = [
        (DWORD, "LowPart"),
        (LONG, "HighPart"),
    ]


class MULTI_SZ(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "Value"),
        (DWORD, "nChar"),
    ]


class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [
        (UNSIGNED_SHORT, "Length"),
        (UNSIGNED_SHORT, "MaximumLength"),
        (PWCHAR, "Buffer"),
    ]


class SERVER_INFO_100(NdrStructure):
    MEMBERS = [
        (DWORD, "sv100_platform_id"),
        (PWCHAR_T, "sv100_name"),
    ]


class SERVER_INFO_101(NdrStructure):
    MEMBERS = [
        (DWORD, "sv101_platform_id"),
        (PWCHAR_T, "sv101_name"),
        (DWORD, "sv101_version_major"),
        (DWORD, "sv101_version_minor"),
        (DWORD, "sv101_version_type"),
        (PWCHAR_T, "sv101_comment"),
    ]


class SYSTEMTIME(NdrStructure):
    MEMBERS = [
        (WORD, "wYear"),
        (WORD, "wMonth"),
        (WORD, "wDayOfWeek"),
        (WORD, "wDay"),
        (WORD, "wHour"),
        (WORD, "wMinute"),
        (WORD, "wSecond"),
        (WORD, "wMilliseconds"),
    ]


class UINT128(NdrStructure):
    MEMBERS = [
        (UINT64, "lower"),
        (UINT64, "upper"),
    ]


class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [
        (UNSIGNED___INT64, "QuadPart"),
    ]


class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [
        (BYTE, "Value"),
    ]


class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [
        (WORD, "Level"),
        (ACCESS_MASK, "Remaining"),
        (PGUID, "ObjectType"),
    ]


class ACE_HEADER(NdrStructure):
    MEMBERS = [
        (UCHAR, "AceType"),
        (UCHAR, "AceFlags"),
        (USHORT, "AceSize"),
    ]


class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [
        (ACE_HEADER, "Header"),
        (ACCESS_MASK, "Mask"),
        (DWORD, "SidStart"),
    ]


class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [
        (DWORD, "Policy"),
    ]


class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [
        (ACCESS_MASK, "AllowedAccess"),
        (BOOLEAN, "WriteAllowed"),
        (BOOLEAN, "ReadAllowed"),
        (BOOLEAN, "ExecuteAllowed"),
        (TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),
    ]


class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [
        (DWORD, "Length"),
        (BYTE, "OctetString"),
    ]


class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (PLONG64, "pInt64"),
        2: (PDWORD64, "pUint64"),
        3: (PWSTR, "ppString"),
        4: (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),
    }


class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [
        (DWORD, "Name"),
        (WORD, "ValueType"),
        (WORD, "Reserved"),
        (DWORD, "Flags"),
        (DWORD, "ValueCount"),
        (VALUES, "Values"),
    ]


class RPC_SID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "Revision"),
        (UNSIGNED_CHAR, "SubAuthorityCount"),
        (RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),
        (UNSIGNED_LONG, "SubAuthority"),
    ]


class ACL(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "AclRevision"),
        (UNSIGNED_CHAR, "Sbz1"),
        (UNSIGNED_SHORT, "AclSize"),
        (UNSIGNED_SHORT, "AceCount"),
        (UNSIGNED_SHORT, "Sbz2"),
    ]


class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [
        (UCHAR, "Revision"),
        (UCHAR, "Sbz1"),
        (USHORT, "Control"),
        (PSID, "Owner"),
        (PSID, "Group"),
        (PACL, "Sacl"),
        (PACL, "Dacl"),
    ]


class FILETIME(NdrStructure):
    MEMBERS = [
        (DWORD, "dwLowDateTime"),
        (DWORD, "dwHighDateTime"),
    ]


class GUID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "Data1"),
        (UNSIGNED_SHORT, "Data2"),
        (UNSIGNED_SHORT, "Data3"),
        (BYTE, "Data4"),
    ]


class LARGE_INTEGER(NdrStructure):
    MEMBERS = [
        (SIGNED___INT64, "QuadPart"),
    ]


class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [
        (USHORT, "Id"),
        (UCHAR, "Version"),
        (UCHAR, "Channel"),
        (UCHAR, "Level"),
        (UCHAR, "Opcode"),
        (USHORT, "Task"),
        (ULONGLONG, "Keyword"),
    ]


class S0(NdrStructure):
    MEMBERS = [
        (ULONG, "KernelTime"),
        (ULONG, "UserTime"),
    ]


class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (S0, "s0"),
        2: (ULONG64, "ProcessorTime"),
    }


class EVENT_HEADER(NdrStructure):
    MEMBERS = [
        (USHORT, "Size"),
        (USHORT, "HeaderType"),
        (USHORT, "Flags"),
        (USHORT, "EventProperty"),
        (ULONG, "ThreadId"),
        (ULONG, "ProcessId"),
        (LARGE_INTEGER, "TimeStamp"),
        (GUID, "ProviderId"),
        (EVENT_DESCRIPTOR, "EventDescriptor"),
        (U0, "u0"),
        (GUID, "ActivityId"),
    ]


class LUID(NdrStructure):
    MEMBERS = [
        (DWORD, "LowPart"),
        (LONG, "HighPart"),
    ]


class MULTI_SZ(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "Value"),
        (DWORD, "nChar"),
    ]


class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [
        (UNSIGNED_SHORT, "Length"),
        (UNSIGNED_SHORT, "MaximumLength"),
        (PWCHAR, "Buffer"),
    ]


class SERVER_INFO_100(NdrStructure):
    MEMBERS = [
        (DWORD, "sv100_platform_id"),
        (PWCHAR_T, "sv100_name"),
    ]


class SERVER_INFO_101(NdrStructure):
    MEMBERS = [
        (DWORD, "sv101_platform_id"),
        (PWCHAR_T, "sv101_name"),
        (DWORD, "sv101_version_major"),
        (DWORD, "sv101_version_minor"),
        (DWORD, "sv101_version_type"),
        (PWCHAR_T, "sv101_comment"),
    ]


class SYSTEMTIME(NdrStructure):
    MEMBERS = [
        (WORD, "wYear"),
        (WORD, "wMonth"),
        (WORD, "wDayOfWeek"),
        (WORD, "wDay"),
        (WORD, "wHour"),
        (WORD, "wMinute"),
        (WORD, "wSecond"),
        (WORD, "wMilliseconds"),
    ]


class UINT128(NdrStructure):
    MEMBERS = [
        (UINT64, "lower"),
        (UINT64, "upper"),
    ]


class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [
        (UNSIGNED___INT64, "QuadPart"),
    ]


class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [
        (BYTE, "Value"),
    ]


class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [
        (WORD, "Level"),
        (ACCESS_MASK, "Remaining"),
        (PGUID, "ObjectType"),
    ]


class ACE_HEADER(NdrStructure):
    MEMBERS = [
        (UCHAR, "AceType"),
        (UCHAR, "AceFlags"),
        (USHORT, "AceSize"),
    ]


class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [
        (ACE_HEADER, "Header"),
        (ACCESS_MASK, "Mask"),
        (DWORD, "SidStart"),
    ]


class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [
        (DWORD, "Policy"),
    ]


class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [
        (ACCESS_MASK, "AllowedAccess"),
        (BOOLEAN, "WriteAllowed"),
        (BOOLEAN, "ReadAllowed"),
        (BOOLEAN, "ExecuteAllowed"),
        (TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),
    ]


class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [
        (DWORD, "Length"),
        (BYTE, "OctetString"),
    ]


class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (PLONG64, "pInt64"),
        2: (PDWORD64, "pUint64"),
        3: (PWSTR, "ppString"),
        4: (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),
    }


class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [
        (DWORD, "Name"),
        (WORD, "ValueType"),
        (WORD, "Reserved"),
        (DWORD, "Flags"),
        (DWORD, "ValueCount"),
        (VALUES, "Values"),
    ]


class RPC_SID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "Revision"),
        (UNSIGNED_CHAR, "SubAuthorityCount"),
        (RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),
        (UNSIGNED_LONG, "SubAuthority"),
    ]


class ACL(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "AclRevision"),
        (UNSIGNED_CHAR, "Sbz1"),
        (UNSIGNED_SHORT, "AclSize"),
        (UNSIGNED_SHORT, "AceCount"),
        (UNSIGNED_SHORT, "Sbz2"),
    ]


class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [
        (UCHAR, "Revision"),
        (UCHAR, "Sbz1"),
        (USHORT, "Control"),
        (PSID, "Owner"),
        (PSID, "Group"),
        (PACL, "Sacl"),
        (PACL, "Dacl"),
    ]


class XACTUOW(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "rgb"),
    ]


class BLOB(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "cbSize"),
        (PUNSIGNED_CHAR, "pBlobData"),
    ]


class CAUB(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "cElems"),
        (PUNSIGNED_CHAR, "pElems"),
    ]


class CAUI(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "cElems"),
        (PUNSIGNED_SHORT, "pElems"),
    ]


class CAL(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "cElems"),
        (PLONG, "pElems"),
    ]


class CAUL(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "cElems"),
        (PUNSIGNED_LONG, "pElems"),
    ]


class CAUH(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "cElems"),
        (PULARGE_INTEGER, "pElems"),
    ]


class CACLSID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "cElems"),
        (PGUID, "pElems"),
    ]


class CALPWSTR(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "cElems"),
        (PPWCHAR_T, "pElems"),
    ]


class CAPROPVARIANT(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "cElems"),
        (PPROPVARIANT, "pElems"),
    ]


class _VARUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        2: (CHAR, "cVal"),
        3: (UCHAR, "bVal"),
        4: (SHORT, "iVal"),
        5: (USHORT, "uiVal"),
        6: (LONG, "lVal"),
        7: (ULONG, "ulVal"),
        8: (LARGE_INTEGER, "hVal"),
        9: (ULARGE_INTEGER, "uhVal"),
        10: (VARIANT_BOOL, "boolVal"),
        11: (PGUID, "puuid"),
        12: (BLOB, "blob"),
        13: (PWCHAR_T, "pwszVal"),
        14: (CAUB, "caub"),
        15: (CAUI, "caui"),
        16: (CAL, "cal"),
        17: (CAUL, "caul"),
        18: (CAUH, "cauh"),
        19: (CACLSID, "cauuid"),
        20: (CALPWSTR, "calpwstr"),
        21: (CAPROPVARIANT, "capropvar"),
    }


class TAG_INNER_PROPVARIANT(NdrStructure):
    MEMBERS = [
        (VARTYPE, "vt"),
        (UCHAR, "wReserved1"),
        (UCHAR, "wReserved2"),
        (ULONG, "wReserved3"),
        (_VARUNION, "_varUnion"),
    ]


class DL_ID(NdrStructure):
    MEMBERS = [
        (GUID, "m_DlGuid"),
        (PWCHAR_T, "m_pwzDomain"),
    ]


class MULTICAST_ID(NdrStructure):
    MEMBERS = [
        (ULONG, "m_address"),
        (ULONG, "m_port"),
    ]


class OBJECTID(NdrStructure):
    MEMBERS = [
        (GUID, "Lineage"),
        (DWORD, "Uniquifier"),
    ]


class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        2: (GUID, "m_gPublicID"),
        3: (OBJECTID, "m_oPrivateID"),
        4: (PWCHAR_T, "m_pDirectID"),
        5: (GUID, "m_gMachineID"),
        6: (GUID, "m_GConnectorID"),
        7: (DL_ID, "m_DlID"),
        8: (MULTICAST_ID, "m_MulticastID"),
        9: (PWCHAR_T, "m_pDirectSubqueueID"),
    }


class QUEUE_FORMAT(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "m_qft"),
        (UNSIGNED_CHAR, "m_SuffixAndFlags"),
        (UNSIGNED_SHORT, "m_reserved"),
        (U0, "u0"),
    ]


Method("R_GetServerPort", In(HANDLE_T),), Method("Opnum1NotUsedOnWire", In(),), Method(
    "R_OpenQueue",
    In(HANDLE_T),
    In(PQUEUE_FORMAT),
    In(DWORD),
    In(DWORD),
    In(PGUID),
    In(LONG),
    In(UNSIGNED_CHAR),
    In(UNSIGNED_CHAR),
    In(USHORT),
    In(LONG),
    Out(PQUEUE_CONTEXT_HANDLE_SERIALIZE),
), Method(
    "R_CloseQueue",
    In(HANDLE_T),
    InOut(PQUEUE_CONTEXT_HANDLE_SERIALIZE),
), Method(
    "R_CreateCursor",
    In(HANDLE_T),
    In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
    Out(PDWORD),
), Method(
    "R_CloseCursor",
    In(HANDLE_T),
    In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
    In(DWORD),
), Method(
    "R_PurgeQueue",
    In(HANDLE_T),
    In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
), Method(
    "R_StartReceive",
    In(HANDLE_T),
    In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
    In(ULONGLONG),
    In(DWORD),
    In(DWORD),
    In(DWORD),
    In(DWORD),
    In(DWORD),
    In(DWORD),
    Out(PDWORD),
    Out(PULONGLONG),
    Out(PDWORD),
    Out(PPSECTIONBUFFER),
), Method(
    "R_CancelReceive",
    In(HANDLE_T),
    In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
    In(DWORD),
), Method(
    "R_EndReceive",
    In(HANDLE_T),
    In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
    In(DWORD),
    In(DWORD),
), Method(
    "R_MoveMessage",
    In(HANDLE_T),
    In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
    In(ULONGLONG),
    In(ULONGLONG),
    In(PXACTUOW),
), Method(
    "R_OpenQueueForMove",
    In(HANDLE_T),
    In(PQUEUE_FORMAT),
    In(DWORD),
    In(DWORD),
    In(PGUID),
    In(LONG),
    In(UNSIGNED_CHAR),
    In(UNSIGNED_CHAR),
    In(USHORT),
    In(LONG),
    Out(PULONGLONG),
    Out(PQUEUE_CONTEXT_HANDLE_SERIALIZE),
), Method(
    "R_QMEnlistRemoteTransaction",
    In(HANDLE_T),
    In(PXACTUOW),
    In(DWORD),
    In(PUNSIGNED_CHAR),
    In(PQUEUE_FORMAT),
), Method(
    "R_StartTransactionalReceive",
    In(HANDLE_T),
    In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
    In(ULONGLONG),
    In(DWORD),
    In(DWORD),
    In(DWORD),
    In(DWORD),
    In(DWORD),
    In(DWORD),
    In(PXACTUOW),
    Out(PDWORD),
    Out(PULONGLONG),
    Out(PDWORD),
    Out(PPSECTIONBUFFER),
), Method(
    "R_SetUserAcknowledgementClass",
    In(HANDLE_T),
    In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
    In(ULONGLONG),
    In(USHORT),
), Method(
    "R_EndTransactionalReceive",
    In(HANDLE_T),
    In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
    In(DWORD),
    In(DWORD),
),
