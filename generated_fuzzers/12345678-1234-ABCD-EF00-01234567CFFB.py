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


Method(
    "NetrLogonUasLogon",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
    Out(PPNETLOGON_VALIDATION_UAS_INFO),
), Method(
    "NetrLogonUasLogoff",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
    Out(PNETLOGON_LOGOFF_UAS_INFO),
), Method(
    "NetrLogonSamLogon",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    InOut(PNETLOGON_AUTHENTICATOR),
    In(NETLOGON_LOGON_INFO_CLASS),
    In(PNETLOGON_LEVEL),
    In(NETLOGON_VALIDATION_INFO_CLASS),
    Out(PNETLOGON_VALIDATION),
    Out(PUCHAR),
), Method(
    "NetrLogonSamLogoff",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    InOut(PNETLOGON_AUTHENTICATOR),
    In(NETLOGON_LOGON_INFO_CLASS),
    In(PNETLOGON_LEVEL),
), Method(
    "NetrServerReqChallenge",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_CREDENTIAL),
    Out(PNETLOGON_CREDENTIAL),
), Method(
    "NetrServerAuthenticate",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(NETLOGON_SECURE_CHANNEL_TYPE),
    In(PWCHAR_T),
    In(PNETLOGON_CREDENTIAL),
    Out(PNETLOGON_CREDENTIAL),
), Method(
    "NetrServerPasswordSet",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(NETLOGON_SECURE_CHANNEL_TYPE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    Out(PNETLOGON_AUTHENTICATOR),
    In(PENCRYPTED_NT_OWF_PASSWORD),
), Method(
    "NetrDatabaseDeltas",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    InOut(PNETLOGON_AUTHENTICATOR),
    In(DWORD),
    InOut(PNLPR_MODIFIED_COUNT),
    Out(PPNETLOGON_DELTA_ENUM_ARRAY),
    In(DWORD),
), Method(
    "NetrDatabaseSync",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    InOut(PNETLOGON_AUTHENTICATOR),
    In(DWORD),
    InOut(PULONG),
    Out(PPNETLOGON_DELTA_ENUM_ARRAY),
    In(DWORD),
), Method(
    "NetrAccountDeltas",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    InOut(PNETLOGON_AUTHENTICATOR),
    In(PUAS_INFO_0),
    In(DWORD),
    In(DWORD),
    Out(PUCHAR),
    In(DWORD),
    Out(PULONG),
    Out(PULONG),
    Out(PUAS_INFO_0),
), Method(
    "NetrAccountSync",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    InOut(PNETLOGON_AUTHENTICATOR),
    In(DWORD),
    In(DWORD),
    Out(PUCHAR),
    In(DWORD),
    Out(PULONG),
    Out(PULONG),
    Out(PULONG),
    Out(PUAS_INFO_0),
), Method(
    "NetrGetDCName",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    Out(PPWCHAR_T),
), Method(
    "NetrLogonControl",
    In(LOGONSRV_HANDLE),
    In(DWORD),
    In(DWORD),
    Out(PNETLOGON_CONTROL_QUERY_INFORMATION),
), Method(
    "NetrGetAnyDCName",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    Out(PPWCHAR_T),
), Method(
    "NetrLogonControl2",
    In(LOGONSRV_HANDLE),
    In(DWORD),
    In(DWORD),
    In(PNETLOGON_CONTROL_DATA_INFORMATION),
    Out(PNETLOGON_CONTROL_QUERY_INFORMATION),
), Method(
    "NetrServerAuthenticate2",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(NETLOGON_SECURE_CHANNEL_TYPE),
    In(PWCHAR_T),
    In(PNETLOGON_CREDENTIAL),
    Out(PNETLOGON_CREDENTIAL),
    InOut(PULONG),
), Method(
    "NetrDatabaseSync2",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    InOut(PNETLOGON_AUTHENTICATOR),
    In(DWORD),
    In(SYNC_STATE),
    InOut(PULONG),
    Out(PPNETLOGON_DELTA_ENUM_ARRAY),
    In(DWORD),
), Method(
    "NetrDatabaseRedo",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    InOut(PNETLOGON_AUTHENTICATOR),
    In(PUCHAR),
    In(DWORD),
    Out(PPNETLOGON_DELTA_ENUM_ARRAY),
), Method(
    "NetrLogonControl2Ex",
    In(LOGONSRV_HANDLE),
    In(DWORD),
    In(DWORD),
    In(PNETLOGON_CONTROL_DATA_INFORMATION),
    Out(PNETLOGON_CONTROL_QUERY_INFORMATION),
), Method(
    "NetrEnumerateTrustedDomains",
    In(LOGONSRV_HANDLE),
    Out(PDOMAIN_NAME_BUFFER),
), Method(
    "DsrGetDcName",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PGUID),
    In(PGUID),
    In(ULONG),
    Out(PPDOMAIN_CONTROLLER_INFOW),
), Method(
    "NetrLogonGetCapabilities",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    InOut(PNETLOGON_AUTHENTICATOR),
    In(DWORD),
    Out(PNETLOGON_CAPABILITIES),
), Method(
    "NetrLogonSetServiceBits",
    In(LOGONSRV_HANDLE),
    In(DWORD),
    In(DWORD),
), Method(
    "NetrLogonGetTrustRid",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    Out(PULONG),
), Method(
    "NetrLogonComputeServerDigest",
    In(LOGONSRV_HANDLE),
    In(ULONG),
    In(PUCHAR),
    In(ULONG),
    Out(CHAR),
    Out(CHAR),
), Method(
    "NetrLogonComputeClientDigest",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PUCHAR),
    In(ULONG),
    Out(CHAR),
    Out(CHAR),
), Method(
    "NetrServerAuthenticate3",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(NETLOGON_SECURE_CHANNEL_TYPE),
    In(PWCHAR_T),
    In(PNETLOGON_CREDENTIAL),
    Out(PNETLOGON_CREDENTIAL),
    InOut(PULONG),
    Out(PULONG),
), Method(
    "DsrGetDcNameEx",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PGUID),
    In(PWCHAR_T),
    In(ULONG),
    Out(PPDOMAIN_CONTROLLER_INFOW),
), Method(
    "DsrGetSiteName",
    In(LOGONSRV_HANDLE),
    Out(PPWCHAR_T),
), Method(
    "NetrLogonGetDomainInfo",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    InOut(PNETLOGON_AUTHENTICATOR),
    In(DWORD),
    In(PNETLOGON_WORKSTATION_INFORMATION),
    Out(PNETLOGON_DOMAIN_INFORMATION),
), Method(
    "NetrServerPasswordSet2",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(NETLOGON_SECURE_CHANNEL_TYPE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    Out(PNETLOGON_AUTHENTICATOR),
    In(PNL_TRUST_PASSWORD),
), Method(
    "NetrServerPasswordGet",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(NETLOGON_SECURE_CHANNEL_TYPE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    Out(PNETLOGON_AUTHENTICATOR),
    Out(PENCRYPTED_NT_OWF_PASSWORD),
), Method(
    "NetrLogonSendToSam",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    Out(PNETLOGON_AUTHENTICATOR),
    In(PUCHAR),
    In(ULONG),
), Method(
    "DsrAddressToSiteNamesW",
    In(LOGONSRV_HANDLE),
    In(DWORD),
    In(PNL_SOCKET_ADDRESS),
    Out(PPNL_SITE_NAME_ARRAY),
), Method(
    "DsrGetDcNameEx2",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(ULONG),
    In(PWCHAR_T),
    In(PGUID),
    In(PWCHAR_T),
    In(ULONG),
    Out(PPDOMAIN_CONTROLLER_INFOW),
), Method(
    "NetrLogonGetTimeServiceParentDomain",
    In(LOGONSRV_HANDLE),
    Out(PPWCHAR_T),
    Out(PINT),
), Method(
    "NetrEnumerateTrustedDomainsEx",
    In(LOGONSRV_HANDLE),
    Out(PNETLOGON_TRUSTED_DOMAIN_ARRAY),
), Method(
    "DsrAddressToSiteNamesExW",
    In(LOGONSRV_HANDLE),
    In(DWORD),
    In(PNL_SOCKET_ADDRESS),
    Out(PPNL_SITE_NAME_EX_ARRAY),
), Method(
    "DsrGetDcSiteCoverageW",
    In(LOGONSRV_HANDLE),
    Out(PPNL_SITE_NAME_ARRAY),
), Method(
    "NetrLogonSamLogonEx",
    In(HANDLE_T),
    In(PWCHAR_T),
    In(PWCHAR_T),
    In(NETLOGON_LOGON_INFO_CLASS),
    In(PNETLOGON_LEVEL),
    In(NETLOGON_VALIDATION_INFO_CLASS),
    Out(PNETLOGON_VALIDATION),
    Out(PUCHAR),
    InOut(PULONG),
), Method(
    "DsrEnumerateDomainTrusts",
    In(LOGONSRV_HANDLE),
    In(ULONG),
    Out(PNETLOGON_TRUSTED_DOMAIN_ARRAY),
), Method(
    "DsrDeregisterDnsHostRecords",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PGUID),
    In(PGUID),
    In(PWCHAR_T),
), Method(
    "NetrServerTrustPasswordsGet",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(NETLOGON_SECURE_CHANNEL_TYPE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    Out(PNETLOGON_AUTHENTICATOR),
    Out(PENCRYPTED_NT_OWF_PASSWORD),
    Out(PENCRYPTED_NT_OWF_PASSWORD),
), Method(
    "DsrGetForestTrustInformation",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(DWORD),
    Out(PPLSA_FOREST_TRUST_INFORMATION),
), Method(
    "NetrGetForestTrustInformation",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    Out(PNETLOGON_AUTHENTICATOR),
    In(DWORD),
    Out(PPLSA_FOREST_TRUST_INFORMATION),
), Method(
    "NetrLogonSamLogonWithFlags",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    InOut(PNETLOGON_AUTHENTICATOR),
    In(NETLOGON_LOGON_INFO_CLASS),
    In(PNETLOGON_LEVEL),
    In(NETLOGON_VALIDATION_INFO_CLASS),
    Out(PNETLOGON_VALIDATION),
    Out(PUCHAR),
    InOut(PULONG),
), Method(
    "NetrServerGetTrustInfo",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(NETLOGON_SECURE_CHANNEL_TYPE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    Out(PNETLOGON_AUTHENTICATOR),
    Out(PENCRYPTED_NT_OWF_PASSWORD),
    Out(PENCRYPTED_NT_OWF_PASSWORD),
    Out(PPNL_GENERIC_RPC_DATA),
), Method(
    "OpnumUnused47",
    In(),
), Method(
    "DsrUpdateReadOnlyServerDnsRecords",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    Out(PNETLOGON_AUTHENTICATOR),
    In(PWCHAR_T),
    In(ULONG),
    InOut(PNL_DNS_NAME_INFO_ARRAY),
), Method(
    "NetrChainSetClientAttributes",
    In(LOGONSRV_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
    In(PNETLOGON_AUTHENTICATOR),
    InOut(PNETLOGON_AUTHENTICATOR),
    In(DWORD),
    In(PNL_IN_CHAIN_SET_CLIENT_ATTRIBUTES),
    InOut(PDWORD),
    InOut(PNL_OUT_CHAIN_SET_CLIENT_ATTRIBUTES),
),
