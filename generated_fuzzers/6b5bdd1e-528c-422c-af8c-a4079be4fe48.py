
from fuzzer.midl import *
from fuzzer.core import *
import .server
BYTE = NdrByte
USHORT = NdrShort
UCHAR = NdrByte
ULONG = NdrLong
ULONG64 = NdrHyper
DWORD64 = NdrHyper
DWORD = NdrLong
UINT64 = NdrHyper
WORD = NdrByte
PWCHAR_T = NdrByte
BOOLEAN = NdrBoolean
__INT64 = NdrHyper
UNSIGNED_SHORT = NdrShort
UNSIGNED_CHAR = NdrByte
UNSIGNED_LONG = NdrLong
UNSIGNEDLONG = NdrLong
UNSIGNED_INT = NdrLong
UNSIGNED___INT64 = NdrHyper
SIGNED___INT64 = NdrHyper
SIGNED_INT = NdrShort
SIGNED_LONG = NdrLong
SIGNED_CHAR = NdrByte
SIGNED_SHORT = NdrShort
WCHAR_T = NdrWString
CHAR = NdrByte
INT = NdrLong
VOID = CONTEXT_HANDLE
LONG = NdrLong
__INT3264 = NdrHyper
UNSIGNED___INT3264 = NdrHyper
UNSIGNED_HYPER = NdrHyper
HYPER = NdrHyper
DWORDLONG = NdrHyper
LONG_PTR = NdrHyper
ULONG_PTR = NdrHyper
LPSTR = NdrCString
LPWSTR = NdrWString
LPCSTR = NdrCString
LPCWSTR = NdrWString
LMSTR = NdrWString
PWSTR = NdrWString
WCHAR = NdrWString
PBYTE = NdrByte

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD, "dwLowDateTime"),(DWORD, "dwHighDateTime"),]

    
PFILETIME = FILETIMELPFILETIME = FILETIME
class GUID(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Data1"),(UNSIGNED_SHORT, "Data2"),(UNSIGNED_SHORT, "Data3"),(BYTE, "Data4"),]

    
UUID = GUIDPGUID = GUID
class LARGE_INTEGER(NdrStructure):
    MEMBERS = [(SIGNED___INT64, "QuadPart"),]

    
PLARGE_INTEGER = LARGE_INTEGER
class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [(USHORT, "Id"),(UCHAR, "Version"),(UCHAR, "Channel"),(UCHAR, "Level"),(UCHAR, "Opcode"),(USHORT, "Task"),(ULONGLONG, "Keyword"),]

    
PEVENT_DESCRIPTOR = EVENT_DESCRIPTORPCEVENT_DESCRIPTOR = EVENT_DESCRIPTOR
class S0(NdrStructure):
    MEMBERS = [(ULONG, "KernelTime"),(ULONG, "UserTime"),]

    

class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (S0, "s0"),2 : (ULONG64, "ProcessorTime"),}

    

class EVENT_HEADER(NdrStructure):
    MEMBERS = [(USHORT, "Size"),(USHORT, "HeaderType"),(USHORT, "Flags"),(USHORT, "EventProperty"),(ULONG, "ThreadId"),(ULONG, "ProcessId"),(LARGE_INTEGER, "TimeStamp"),(GUID, "ProviderId"),(EVENT_DESCRIPTOR, "EventDescriptor"),(U0, "u0"),(GUID, "ActivityId"),]

    
PEVENT_HEADER = EVENT_HEADER
class LUID(NdrStructure):
    MEMBERS = [(DWORD, "LowPart"),(LONG, "HighPart"),]

    
PLUID = LUID
class MULTI_SZ(NdrStructure):
    MEMBERS = [(PWCHAR_T, "Value"),(DWORD, "nChar"),]

    

class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Length"),(UNSIGNED_SHORT, "MaximumLength"),(PWCHAR, "Buffer"),]

    
PRPC_UNICODE_STRING = RPC_UNICODE_STRING
class SERVER_INFO_100(NdrStructure):
    MEMBERS = [(DWORD, "sv100_platform_id"),(PWCHAR_T, "sv100_name"),]

    
PSERVER_INFO_100 = SERVER_INFO_100LPSERVER_INFO_100 = SERVER_INFO_100
class SERVER_INFO_101(NdrStructure):
    MEMBERS = [(DWORD, "sv101_platform_id"),(PWCHAR_T, "sv101_name"),(DWORD, "sv101_version_major"),(DWORD, "sv101_version_minor"),(DWORD, "sv101_version_type"),(PWCHAR_T, "sv101_comment"),]

    
PSERVER_INFO_101 = SERVER_INFO_101LPSERVER_INFO_101 = SERVER_INFO_101
class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD, "wYear"),(WORD, "wMonth"),(WORD, "wDayOfWeek"),(WORD, "wDay"),(WORD, "wHour"),(WORD, "wMinute"),(WORD, "wSecond"),(WORD, "wMilliseconds"),]

    
PSYSTEMTIME = SYSTEMTIME
class UINT128(NdrStructure):
    MEMBERS = [(UINT64, "lower"),(UINT64, "upper"),]

    
PUINT128 = UINT128
class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [(UNSIGNED___INT64, "QuadPart"),]

    
PULARGE_INTEGER = ULARGE_INTEGER
class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [(BYTE, "Value"),]

    

class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [(WORD, "Level"),(ACCESS_MASK, "Remaining"),(PGUID, "ObjectType"),]

    
POBJECT_TYPE_LIST = OBJECT_TYPE_LIST
class ACE_HEADER(NdrStructure):
    MEMBERS = [(UCHAR, "AceType"),(UCHAR, "AceFlags"),(USHORT, "AceSize"),]

    
PACE_HEADER = ACE_HEADER
class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [(ACE_HEADER, "Header"),(ACCESS_MASK, "Mask"),(DWORD, "SidStart"),]

    
PSYSTEM_MANDATORY_LABEL_ACE = SYSTEM_MANDATORY_LABEL_ACE
class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [(DWORD, "Policy"),]

    
PTOKEN_MANDATORY_POLICY = TOKEN_MANDATORY_POLICY
class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [(ACCESS_MASK, "AllowedAccess"),(BOOLEAN, "WriteAllowed"),(BOOLEAN, "ReadAllowed"),(BOOLEAN, "ExecuteAllowed"),(TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),]

    
PMANDATORY_INFORMATION = MANDATORY_INFORMATION
class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [(DWORD, "Length"),(BYTE, "OctetString"),]

    
PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE = CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE
class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PLONG64, "pInt64"),2 : (PDWORD64, "pUint64"),3 : (PWSTR, "ppString"),4 : (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),}

    

class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [(DWORD, "Name"),(WORD, "ValueType"),(WORD, "Reserved"),(DWORD, "Flags"),(DWORD, "ValueCount"),(VALUES, "Values"),]

    
PCLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1 = CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1
class RPC_SID(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "Revision"),(UNSIGNED_CHAR, "SubAuthorityCount"),(RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),(UNSIGNED_LONG, "SubAuthority"),]

    
PRPC_SID = RPC_SIDPSID = RPC_SID
class ACL(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "AclRevision"),(UNSIGNED_CHAR, "Sbz1"),(UNSIGNED_SHORT, "AclSize"),(UNSIGNED_SHORT, "AceCount"),(UNSIGNED_SHORT, "Sbz2"),]

    
PACL = ACL
class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [(UCHAR, "Revision"),(UCHAR, "Sbz1"),(USHORT, "Control"),(PSID, "Owner"),(PSID, "Group"),(PACL, "Sacl"),(PACL, "Dacl"),]

    
PSECURITY_DESCRIPTOR = SECURITY_DESCRIPTOR
class FW_IPV4_SUBNET(NdrStructure):
    MEMBERS = [(DWORD, "dwAddress"),(DWORD, "dwSubNetMask"),]

    
PFW_IPV4_SUBNET = FW_IPV4_SUBNET
class FW_IPV4_SUBNET_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(PFW_IPV4_SUBNET, "pSubNets"),]

    
PFW_IPV4_SUBNET_LIST = FW_IPV4_SUBNET_LIST
class FW_IPV6_SUBNET(NdrStructure):
    MEMBERS = [(BYTE, "Address"),(DWORD, "dwNumPrefixBits"),]

    
PFW_IPV6_SUBNET = FW_IPV6_SUBNET
class FW_IPV6_SUBNET_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(PFW_IPV6_SUBNET, "pSubNets"),]

    
PFW_IPV6_SUBNET_LIST = FW_IPV6_SUBNET_LIST
class FW_IPV4_ADDRESS_RANGE(NdrStructure):
    MEMBERS = [(DWORD, "dwBegin"),(DWORD, "dwEnd"),]

    
PFW_IPV4_ADDRESS_RANGE = FW_IPV4_ADDRESS_RANGE
class FW_IPV6_ADDRESS_RANGE(NdrStructure):
    MEMBERS = [(BYTE, "Begin"),(BYTE, "End"),]

    
PFW_IPV6_ADDRESS_RANGE = FW_IPV6_ADDRESS_RANGE
class FW_IPV4_RANGE_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(PFW_IPV4_ADDRESS_RANGE, "pRanges"),]

    
PFW_IPV4_RANGE_LIST = FW_IPV4_RANGE_LIST
class FW_IPV6_RANGE_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(PFW_IPV6_ADDRESS_RANGE, "pRanges"),]

    
PFW_IPV6_RANGE_LIST = FW_IPV6_RANGE_LIST
class FW_PORT_RANGE(NdrStructure):
    MEMBERS = [(WORD, "wBegin"),(WORD, "wEnd"),]

    
PFW_PORT_RANGE = FW_PORT_RANGE
class FW_PORT_RANGE_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(PFW_PORT_RANGE, "pPorts"),]

    
PFW_PORT_RANGE_LIST = FW_PORT_RANGE_LIST
class FW_PORTS(NdrStructure):
    MEMBERS = [(WORD, "wPortKeywords"),(FW_PORT_RANGE_LIST, "Ports"),]

    
PFW_PORTS = FW_PORTS
class FW_ICMP_TYPE_CODE(NdrStructure):
    MEMBERS = [(BYTE, "bType"),(WORD, "wCode"),]

    
PFW_ICMP_TYPE_CODE = FW_ICMP_TYPE_CODE
class FW_ICMP_TYPE_CODE_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(PFW_ICMP_TYPE_CODE, "pEntries"),]

    
PFW_ICMP_TYPE_CODE_LIST = FW_ICMP_TYPE_CODE_LIST
class FW_INTERFACE_LUIDS(NdrStructure):
    MEMBERS = [(DWORD, "dwNumLUIDs"),(PGUID, "pLUIDs"),]

    
PFW_INTERFACE_LUIDS = FW_INTERFACE_LUIDS
class FW_ADDRESSES(NdrStructure):
    MEMBERS = [(DWORD, "dwV4AddressKeywords"),(DWORD, "dwV6AddressKeywords"),(FW_IPV4_SUBNET_LIST, "V4SubNets"),(FW_IPV4_RANGE_LIST, "V4Ranges"),(FW_IPV6_SUBNET_LIST, "V6SubNets"),(FW_IPV6_RANGE_LIST, "V6Ranges"),]

    
PFW_ADDRESSES = FW_ADDRESSES
class FW_OBJECT_METADATA(NdrStructure):
    MEMBERS = [(UINT64, "qwFilterContextID"),(DWORD, "dwNumEntries"),(PFW_ENFORCEMENT_STATE, "pEnforcementStates"),]

    
PFW_OBJECT_METADATA = FW_OBJECT_METADATA
class FW_OS_PLATFORM(NdrStructure):
    MEMBERS = [(BYTE, "bPlatform"),(BYTE, "bMajorVersion"),(BYTE, "bMinorVersion"),(BYTE, "Reserved"),]

    
PFW_OS_PLATFORM = FW_OS_PLATFORM
class FW_OS_PLATFORM_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(PFW_OS_PLATFORM, "pPlatforms"),]

    
PFW_OS_PLATFORM_LIST = FW_OS_PLATFORM_LIST
class FW_NETWORK_NAMES(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(PLPWSTR, "wszNames"),]

    
PFW_NETWORK_NAMES = FW_NETWORK_NAMES
class FW_RULE2_0(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(PWCHAR, "wszRuleId"),(PWCHAR, "wszName"),(PWCHAR, "wszDescription"),(DWORD, "dwProfiles"),(FW_DIRECTION, "Direction"),(WORD, "wIpProtocol"),(U0, "u0"),(FW_ADDRESSES, "LocalAddresses"),(FW_ADDRESSES, "RemoteAddresses"),(FW_INTERFACE_LUIDS, "LocalInterfaceIds"),(DWORD, "dwLocalInterfaceTypes"),(PWCHAR, "wszLocalApplication"),(PWCHAR, "wszLocalService"),(FW_RULE_ACTION, "Action"),(WORD, "wFlags"),(PWCHAR, "wszRemoteMachineAuthorizationList"),(PWCHAR, "wszRemoteUserAuthorizationList"),(PWCHAR, "wszEmbeddedContext"),(FW_OS_PLATFORM_LIST, "PlatformValidityList"),(FW_RULE_STATUS, "Status"),(FW_RULE_ORIGIN_TYPE, "Origin"),(PWCHAR, "wszGPOName"),(DWORD, "Reserved"),]

    
PFW_RULE2_0 = FW_RULE2_0
class FW_RULE2_10(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(LPWSTR, "wszRuleId"),(LPWSTR, "wszName"),(LPWSTR, "wszDescription"),(DWORD, "dwProfiles"),(FW_DIRECTION, "Direction"),(WORD, "wIpProtocol"),(U0, "u0"),(FW_ADDRESSES, "LocalAddresses"),(FW_ADDRESSES, "RemoteAddresses"),(FW_INTERFACE_LUIDS, "LocalInterfaceIds"),(DWORD, "dwLocalInterfaceTypes"),(LPWSTR, "wszLocalApplication"),(LPWSTR, "wszLocalService"),(FW_RULE_ACTION, "Action"),(WORD, "wFlags"),(LPWSTR, "wszRemoteMachineAuthorizationList"),(LPWSTR, "wszRemoteUserAuthorizationList"),(LPWSTR, "wszEmbeddedContext"),(FW_OS_PLATFORM_LIST, "PlatformValidityList"),(FW_RULE_STATUS, "Status"),(FW_RULE_ORIGIN_TYPE, "Origin"),(LPWSTR, "wszGPOName"),(DWORD, "Reserved"),(PFW_OBJECT_METADATA, "pMetaData"),]

    
PFW_RULE2_10 = FW_RULE2_10
class FW_RULE2_20(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(LPWSTR, "wszRuleId"),(LPWSTR, "wszName"),(LPWSTR, "wszDescription"),(DWORD, "dwProfiles"),(FW_DIRECTION, "Direction"),(WORD, "wIpProtocol"),(U0, "u0"),(FW_ADDRESSES, "LocalAddresses"),(FW_ADDRESSES, "RemoteAddresses"),(FW_INTERFACE_LUIDS, "LocalInterfaceIds"),(DWORD, "dwLocalInterfaceTypes"),(LPWSTR, "wszLocalApplication"),(LPWSTR, "wszLocalService"),(FW_RULE_ACTION, "Action"),(WORD, "wFlags"),(LPWSTR, "wszRemoteMachineAuthorizationList"),(LPWSTR, "wszRemoteUserAuthorizationList"),(LPWSTR, "wszEmbeddedContext"),(FW_OS_PLATFORM_LIST, "PlatformValidityList"),(FW_RULE_STATUS, "Status"),(FW_RULE_ORIGIN_TYPE, "Origin"),(LPWSTR, "wszGPOName"),(DWORD, "Reserved"),(PFW_OBJECT_METADATA, "pMetaData"),(PWCHAR, "wszLocalUserAuthorizationList"),(PWCHAR, "wszPackageId"),(PWCHAR, "wszLocalUserOwner"),(DWORD, "dwTrustTupleKeywords"),]

    
PFW_RULE2_20 = FW_RULE2_20
class FW_RULE2_24(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(LPWSTR, "wszRuleId"),(LPWSTR, "wszName"),(LPWSTR, "wszDescription"),(DWORD, "dwProfiles"),(FW_DIRECTION, "Direction"),(WORD, "wIpProtocol"),(U0, "u0"),(FW_ADDRESSES, "LocalAddresses"),(FW_ADDRESSES, "RemoteAddresses"),(FW_INTERFACE_LUIDS, "LocalInterfaceIds"),(DWORD, "dwLocalInterfaceTypes"),(LPWSTR, "wszLocalApplication"),(LPWSTR, "wszLocalService"),(FW_RULE_ACTION, "Action"),(WORD, "wFlags"),(LPWSTR, "wszRemoteMachineAuthorizationList"),(LPWSTR, "wszRemoteUserAuthorizationList"),(LPWSTR, "wszEmbeddedContext"),(FW_OS_PLATFORM_LIST, "PlatformValidityList"),(FW_RULE_STATUS, "Status"),(FW_RULE_ORIGIN_TYPE, "Origin"),(LPWSTR, "wszGPOName"),(DWORD, "Reserved"),(PFW_OBJECT_METADATA, "pMetaData"),(PWCHAR, "wszLocalUserAuthorizationList"),(PWCHAR, "wszPackageId"),(PWCHAR, "wszLocalUserOwner"),(DWORD, "dwTrustTupleKeywords"),(FW_NETWORK_NAMES, "OnNetworkNames"),(PWCHAR, "wszSecurityRealmId"),]

    
PFW_RULE2_24 = FW_RULE2_24
class FW_RULE2_25(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(LPWSTR, "wszRuleId"),(LPWSTR, "wszName"),(LPWSTR, "wszDescription"),(DWORD, "dwProfiles"),(FW_DIRECTION, "Direction"),(WORD, "wIpProtocol"),(U0, "u0"),(FW_ADDRESSES, "LocalAddresses"),(FW_ADDRESSES, "RemoteAddresses"),(FW_INTERFACE_LUIDS, "LocalInterfaceIds"),(DWORD, "dwLocalInterfaceTypes"),(LPWSTR, "wszLocalApplication"),(LPWSTR, "wszLocalService"),(FW_RULE_ACTION, "Action"),(WORD, "wFlags"),(LPWSTR, "wszRemoteMachineAuthorizationList"),(LPWSTR, "wszRemoteUserAuthorizationList"),(LPWSTR, "wszEmbeddedContext"),(FW_OS_PLATFORM_LIST, "PlatformValidityList"),(FW_RULE_STATUS, "Status"),(FW_RULE_ORIGIN_TYPE, "Origin"),(LPWSTR, "wszGPOName"),(DWORD, "Reserved"),(PFW_OBJECT_METADATA, "pMetaData"),(PWCHAR, "wszLocalUserAuthorizationList"),(PWCHAR, "wszPackageId"),(PWCHAR, "wszLocalUserOwner"),(DWORD, "dwTrustTupleKeywords"),(FW_NETWORK_NAMES, "OnNetworkNames"),(PWCHAR, "wszSecurityRealmId"),(WORD, "wFlags2"),]

    
PFW_RULE2_25 = FW_RULE2_25
class FW_RULE2_26(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(LPWSTR, "wszRuleId"),(LPWSTR, "wszName"),(LPWSTR, "wszDescription"),(DWORD, "dwProfiles"),(FW_DIRECTION, "Direction"),(WORD, "wIpProtocol"),(U0, "u0"),(FW_ADDRESSES, "LocalAddresses"),(FW_ADDRESSES, "RemoteAddresses"),(FW_INTERFACE_LUIDS, "LocalInterfaceIds"),(DWORD, "dwLocalInterfaceTypes"),(LPWSTR, "wszLocalApplication"),(LPWSTR, "wszLocalService"),(FW_RULE_ACTION, "Action"),(WORD, "wFlags"),(LPWSTR, "wszRemoteMachineAuthorizationList"),(LPWSTR, "wszRemoteUserAuthorizationList"),(LPWSTR, "wszEmbeddedContext"),(FW_OS_PLATFORM_LIST, "PlatformValidityList"),(FW_RULE_STATUS, "Status"),(FW_RULE_ORIGIN_TYPE, "Origin"),(LPWSTR, "wszGPOName"),(DWORD, "Reserved"),(PFW_OBJECT_METADATA, "pMetaData"),(PWCHAR, "wszLocalUserAuthorizationList"),(PWCHAR, "wszPackageId"),(PWCHAR, "wszLocalUserOwner"),(DWORD, "dwTrustTupleKeywords"),(FW_NETWORK_NAMES, "OnNetworkNames"),(PWCHAR, "wszSecurityRealmId"),(WORD, "wFlags2"),(FW_NETWORK_NAMES, "RemoteOutServerNames"),]

    
PFW_RULE2_26 = FW_RULE2_26
class FW_RULE2_27(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(UNSIGNED_SHORT, "wSchemaVersion"),(PWCHAR_T, "wszRuleId"),(PWCHAR_T, "wszName"),(PWCHAR_T, "wszDescription"),(UNSIGNED_LONG, "dwProfiles"),(FW_DIRECTION, "Direction"),(UNSIGNED_SHORT, "wIpProtocol"),(U0, "u0"),(FW_ADDRESSES, "LocalAddresses"),(FW_ADDRESSES, "RemoteAddresses"),(FW_INTERFACE_LUIDS, "LocalInterfaceIds"),(UNSIGNED_LONG, "dwLocalInterfaceTypes"),(PWCHAR_T, "wszLocalApplication"),(PWCHAR_T, "wszLocalService"),(FW_RULE_ACTION, "Action"),(UNSIGNED_SHORT, "wFlags"),(PWCHAR_T, "wszRemoteMachineAuthorizationList"),(PWCHAR_T, "wszRemoteUserAuthorizationList"),(PWCHAR_T, "wszEmbeddedContext"),(FW_OS_PLATFORM_LIST, "PlatformValidityList"),(FW_RULE_STATUS, "Status"),(FW_RULE_ORIGIN_TYPE, "Origin"),(PWCHAR_T, "wszGPOName"),(UNSIGNED_LONG, "Reserved"),(PFW_OBJECT_METADATA, "pMetaData"),(PWCHAR, "wszLocalUserAuthorizationList"),(PWCHAR, "wszPackageId"),(PWCHAR, "wszLocalUserOwner"),(UNSIGNED_LONG, "dwTrustTupleKeywords"),(FW_NETWORK_NAMES, "OnNetworkNames"),(PWCHAR, "wszSecurityRealmId"),(UNSIGNED_SHORT, "wFlags2"),(FW_NETWORK_NAMES, "RemoteOutServerNames"),(PWCHAR, "wszFqbn"),(UNSIGNED_LONG, "compartmentId"),]

    
PFW_RULE2_27 = FW_RULE2_27
class FW_DYNAMIC_KEYWORD_ADDRESS_ID_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwNumIds"),(PUINT32, "ids"),]

    
PFW_DYNAMIC_KEYWORD_ADDRESS_ID_LIST = FW_DYNAMIC_KEYWORD_ADDRESS_ID_LIST
class FW_RULE(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(LPWSTR, "wszRuleId"),(LPWSTR, "wszName"),(LPWSTR, "wszDescription"),(DWORD, "dwProfiles"),(FW_DIRECTION, "Direction"),(WORD, "wIpProtocol"),(U0, "u0"),(FW_ADDRESSES, "LocalAddresses"),(FW_ADDRESSES, "RemoteAddresses"),(FW_INTERFACE_LUIDS, "LocalInterfaceIds"),(DWORD, "dwLocalInterfaceTypes"),(LPWSTR, "wszLocalApplication"),(LPWSTR, "wszLocalService"),(FW_RULE_ACTION, "Action"),(WORD, "wFlags"),(LPWSTR, "wszRemoteMachineAuthorizationList"),(LPWSTR, "wszRemoteUserAuthorizationList"),(LPWSTR, "wszEmbeddedContext"),(FW_OS_PLATFORM_LIST, "PlatformValidityList"),(FW_RULE_STATUS, "Status"),(FW_RULE_ORIGIN_TYPE, "Origin"),(LPWSTR, "wszGPOName"),(DWORD, "Reserved"),(PFW_OBJECT_METADATA, "pMetaData"),(PWCHAR, "wszLocalUserAuthorizationList"),(PWCHAR, "wszPackageId"),(PWCHAR, "wszLocalUserOwner"),(DWORD, "dwTrustTupleKeywords"),(FW_NETWORK_NAMES, "OnNetworkNames"),(PWCHAR, "wszSecurityRealmId"),(WORD, "wFlags2"),(FW_NETWORK_NAMES, "RemoteOutServerNames"),(PWCHAR, "wszFqbn"),(DWORD, "compartmentId"),(GUID, "providerContextKey"),(FW_DYNAMIC_KEYWORD_ADDRESS_ID_LIST, "RemoteDynamicKeywordAddresses"),]

    
PFW_RULE = FW_RULE
class FW_NETWORK(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pszName"),(FW_PROFILE_TYPE, "ProfileType"),]

    
PFW_NETWORK = FW_NETWORK
class FW_ADAPTER(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pszFriendlyName"),(GUID, "Guid"),]

    
PFW_ADAPTER = FW_ADAPTER
class FW_DIAG_APP(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pszAppPath"),]

    
PFW_DIAG_APP = FW_DIAG_APP
class FW_PRODUCT(NdrStructure):
    MEMBERS = [(DWORD, "dwFlags"),(DWORD, "dwNumRuleCategories"),(PFW_RULE_CATEGORY, "pRuleCategories"),(PWCHAR_T, "pszDisplayName"),(PWCHAR_T, "pszPathToSignedProductExe"),]

    
PFW_PRODUCT = FW_PRODUCT
class FW_CS_RULE2_0(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(PWCHAR, "wszRuleId"),(PWCHAR, "wszName"),(PWCHAR, "wszDescription"),(DWORD, "dwProfiles"),(FW_ADDRESSES, "Endpoint1"),(FW_ADDRESSES, "Endpoint2"),(FW_INTERFACE_LUIDS, "LocalInterfaceIds"),(DWORD, "dwLocalInterfaceTypes"),(DWORD, "dwLocalTunnelEndpointV4"),(BYTE, "LocalTunnelEndpointV6"),(DWORD, "dwRemoteTunnelEndpointV4"),(BYTE, "RemoteTunnelEndpointV6"),(FW_PORTS, "Endpoint1Ports"),(FW_PORTS, "Endpoint2Ports"),(WORD, "wIpProtocol"),(PWCHAR, "wszPhase1AuthSet"),(PWCHAR, "wszPhase2CryptoSet"),(PWCHAR, "wszPhase2AuthSet"),(FW_CS_RULE_ACTION, "Action"),(WORD, "wFlags"),(PWCHAR, "wszEmbeddedContext"),(FW_OS_PLATFORM_LIST, "PlatformValidityList"),(FW_RULE_ORIGIN_TYPE, "Origin"),(PWCHAR, "wszGPOName"),(FW_RULE_STATUS, "Status"),]

    
PFW_CS_RULE2_0 = FW_CS_RULE2_0
class FW_CS_RULE2_10(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(PWCHAR, "wszRuleId"),(PWCHAR, "wszName"),(PWCHAR, "wszDescription"),(DWORD, "dwProfiles"),(FW_ADDRESSES, "Endpoint1"),(FW_ADDRESSES, "Endpoint2"),(FW_INTERFACE_LUIDS, "LocalInterfaceIds"),(DWORD, "dwLocalInterfaceTypes"),(DWORD, "dwLocalTunnelEndpointV4"),(BYTE, "LocalTunnelEndpointV6"),(DWORD, "dwRemoteTunnelEndpointV4"),(BYTE, "RemoteTunnelEndpointV6"),(FW_PORTS, "Endpoint1Ports"),(FW_PORTS, "Endpoint2Ports"),(WORD, "wIpProtocol"),(PWCHAR, "wszPhase1AuthSet"),(PWCHAR, "wszPhase2CryptoSet"),(PWCHAR, "wszPhase2AuthSet"),(FW_CS_RULE_ACTION, "Action"),(WORD, "wFlags"),(PWCHAR, "wszEmbeddedContext"),(FW_OS_PLATFORM_LIST, "PlatformValidityList"),(FW_RULE_ORIGIN_TYPE, "Origin"),(PWCHAR, "wszGPOName"),(FW_RULE_STATUS, "Status"),(PWCHAR, "wszMMParentRuleId"),(DWORD, "Reserved"),(PFW_OBJECT_METADATA, "pMetaData"),]

    
PFW_CS_RULE2_10 = FW_CS_RULE2_10
class FW_CS_RULE(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(PWCHAR, "wszRuleId"),(PWCHAR, "wszName"),(PWCHAR, "wszDescription"),(DWORD, "dwProfiles"),(FW_ADDRESSES, "Endpoint1"),(FW_ADDRESSES, "Endpoint2"),(FW_INTERFACE_LUIDS, "LocalInterfaceIds"),(DWORD, "dwLocalInterfaceTypes"),(DWORD, "dwLocalTunnelEndpointV4"),(BYTE, "LocalTunnelEndpointV6"),(DWORD, "dwRemoteTunnelEndpointV4"),(BYTE, "RemoteTunnelEndpointV6"),(FW_PORTS, "Endpoint1Ports"),(FW_PORTS, "Endpoint2Ports"),(WORD, "wIpProtocol"),(PWCHAR, "wszPhase1AuthSet"),(PWCHAR, "wszPhase2CryptoSet"),(PWCHAR, "wszPhase2AuthSet"),(FW_CS_RULE_ACTION, "Action"),(WORD, "wFlags"),(PWCHAR, "wszEmbeddedContext"),(FW_OS_PLATFORM_LIST, "PlatformValidityList"),(FW_RULE_ORIGIN_TYPE, "Origin"),(PWCHAR, "wszGPOName"),(FW_RULE_STATUS, "Status"),(PWCHAR, "wszMMParentRuleId"),(DWORD, "Reserved"),(PFW_OBJECT_METADATA, "pMetaData"),(PWCHAR, "wszRemoteTunnelEndpointFqdn"),(FW_ADDRESSES, "RemoteTunnelEndpoints"),(DWORD, "dwKeyModules"),(DWORD, "FwdPathSALifetime"),(LPWSTR, "wszTransportMachineAuthzSDDL"),(LPWSTR, "wszTransportUserAuthzSDDL"),]

    
PFW_CS_RULE = FW_CS_RULE
class FW_AUTH_SUITE2_10(NdrStructure):
    MEMBERS = [(FW_AUTH_METHOD, "Method"),(WORD, "wFlags"),(U0, "u0"),]

    
PFW_AUTH_SUITE2_10 = FW_AUTH_SUITE2_10
class FW_CERT_CRITERIA(NdrStructure):
    MEMBERS = [(WORD, "wSchemaVersion"),(WORD, "wFlags"),(FW_CERT_CRITERIA_TYPE, "CertCriteriaType"),(FW_CERT_CRITERIA_NAME_TYPE, "NameType"),(LPWSTR, "wszName"),(DWORD, "dwNumEku"),(PLPSTR, "ppEku"),(LPWSTR, "wszHash"),]

    
PFW_CERT_CRITERIA = FW_CERT_CRITERIA
class FW_AUTH_SUITE(NdrStructure):
    MEMBERS = [(FW_AUTH_METHOD, "Method"),(WORD, "wFlags"),(U0, "u0"),]

    
PFW_AUTH_SUITE = FW_AUTH_SUITE
class FW_AUTH_SET2_10(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(FW_IPSEC_PHASE, "IpSecPhase"),(PWCHAR, "wszSetId"),(PWCHAR, "wszName"),(PWCHAR, "wszDescription"),(PWCHAR, "wszEmbeddedContext"),(DWORD, "dwNumSuites"),(PFW_AUTH_SUITE2_10, "pSuites"),(FW_RULE_ORIGIN_TYPE, "Origin"),(PWCHAR, "wszGPOName"),(FW_RULE_STATUS, "Status"),(DWORD, "dwAuthSetFlags"),]

    
PFW_AUTH_SET2_10 = FW_AUTH_SET2_10
class FW_AUTH_SET(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(FW_IPSEC_PHASE, "IpSecPhase"),(PWCHAR, "wszSetId"),(PWCHAR, "wszName"),(PWCHAR, "wszDescription"),(PWCHAR, "wszEmbeddedContext"),(DWORD, "dwNumSuites"),(PFW_AUTH_SUITE, "pSuites"),(FW_RULE_ORIGIN_TYPE, "Origin"),(PWCHAR, "wszGPOName"),(FW_RULE_STATUS, "Status"),(DWORD, "dwAuthSetFlags"),]

    
PFW_AUTH_SET = FW_AUTH_SET
class FW_PHASE1_CRYPTO_SUITE(NdrStructure):
    MEMBERS = [(FW_CRYPTO_KEY_EXCHANGE_TYPE, "KeyExchange"),(FW_CRYPTO_ENCRYPTION_TYPE, "Encryption"),(FW_CRYPTO_HASH_TYPE, "Hash"),(DWORD, "dwP1CryptoSuiteFlags"),]

    
PFW_PHASE1_CRYPTO_SUITE = FW_PHASE1_CRYPTO_SUITE
class FW_PHASE2_CRYPTO_SUITE(NdrStructure):
    MEMBERS = [(FW_CRYPTO_PROTOCOL_TYPE, "Protocol"),(FW_CRYPTO_HASH_TYPE, "AhHash"),(FW_CRYPTO_HASH_TYPE, "EspHash"),(FW_CRYPTO_ENCRYPTION_TYPE, "Encryption"),(DWORD, "dwTimeoutMinutes"),(DWORD, "dwTimeoutKBytes"),(DWORD, "dwP2CryptoSuiteFlags"),]

    
PFW_PHASE2_CRYPTO_SUITE = FW_PHASE2_CRYPTO_SUITE
class FW_CRYPTO_SET(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(FW_IPSEC_PHASE, "IpSecPhase"),(PWCHAR, "wszSetId"),(PWCHAR, "wszName"),(PWCHAR, "wszDescription"),(PWCHAR, "wszEmbeddedContext"),(U0, "u0"),(FW_RULE_ORIGIN_TYPE, "Origin"),(PWCHAR, "wszGPOName"),(FW_RULE_STATUS, "Status"),(DWORD, "dwCryptoSetFlags"),]

    
PFW_CRYPTO_SET = FW_CRYPTO_SET
class FW_BYTE_BLOB(NdrStructure):
    MEMBERS = [(DWORD, "dwSize"),(PBYTE, "Blob"),]

    
PFW_BYTE_BLOB = FW_BYTE_BLOB
class FW_COOKIE_PAIR(NdrStructure):
    MEMBERS = [(UINT64, "Initiator"),(UINT64, "Responder"),]

    
PFW_COOKIE_PAIR = FW_COOKIE_PAIR
class FW_CERT_INFO(NdrStructure):
    MEMBERS = [(FW_BYTE_BLOB, "SubjectName"),(DWORD, "dwCertFlags"),]

    
PFW_CERT_INFO = FW_CERT_INFO
class FW_AUTH_INFO(NdrStructure):
    MEMBERS = [(FW_AUTH_METHOD, "AuthMethod"),(U0, "u0"),(DWORD, "dwAuthInfoFlags"),]

    
PFW_AUTH_INFO = FW_AUTH_INFO
class FW_ENDPOINTS(NdrStructure):
    MEMBERS = [(FW_IP_VERSION, "IpVersion"),(DWORD, "dwSourceV4Address"),(DWORD, "dwDestinationV4Address"),(BYTE, "SourceV6Address"),(BYTE, "DestinationV6Address"),]

    
PFW_ENDPOINTS = FW_ENDPOINTS
class FW_PHASE1_SA_DETAILS(NdrStructure):
    MEMBERS = [(UINT64, "SaId"),(FW_PHASE1_KEY_MODULE_TYPE, "KeyModuleType"),(FW_ENDPOINTS, "Endpoints"),(FW_PHASE1_CRYPTO_SUITE, "SelectedProposal"),(DWORD, "dwProposalLifetimeKBytes"),(DWORD, "dwProposalLifetimeMinutes"),(DWORD, "dwProposalMaxNumPhase2"),(FW_COOKIE_PAIR, "CookiePair"),(PFW_AUTH_INFO, "pFirstAuth"),(PFW_AUTH_INFO, "pSecondAuth"),(DWORD, "dwP1SaFlags"),]

    
PFW_PHASE1_SA_DETAILS = FW_PHASE1_SA_DETAILS
class FW_PHASE2_SA_DETAILS(NdrStructure):
    MEMBERS = [(UINT64, "SaId"),(FW_DIRECTION, "Direction"),(FW_ENDPOINTS, "Endpoints"),(WORD, "wLocalPort"),(WORD, "wRemotePort"),(WORD, "wIpProtocol"),(FW_PHASE2_CRYPTO_SUITE, "SelectedProposal"),(FW_PHASE2_CRYPTO_PFS, "Pfs"),(GUID, "TransportFilterId"),(DWORD, "dwP2SaFlags"),]

    
PFW_PHASE2_SA_DETAILS = FW_PHASE2_SA_DETAILS
class FW_PROFILE_CONFIG_VALUE(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PWCHAR, "wszStr"),2 : (PFW_INTERFACE_LUIDS, "pDisabledInterfaces"),3 : (PDWORD, "pdwVal"),}

    
PFW_PROFILE_CONFIG_VALUE = FW_PROFILE_CONFIG_VALUE
class FW_MM_RULE(NdrStructure):
    MEMBERS = [(PPNEXT, "*pNext"),(WORD, "wSchemaVersion"),(PWCHAR, "wszRuleId"),(PWCHAR, "wszName"),(PWCHAR, "wszDescription"),(DWORD, "dwProfiles"),(FW_ADDRESSES, "Endpoint1"),(FW_ADDRESSES, "Endpoint2"),(PWCHAR, "wszPhase1AuthSet"),(PWCHAR, "wszPhase1CryptoSet"),(WORD, "wFlags"),(PWCHAR, "wszEmbeddedContext"),(FW_OS_PLATFORM_LIST, "PlatformValidityList"),(FW_RULE_ORIGIN_TYPE, "Origin"),(PWCHAR, "wszGPOName"),(FW_RULE_STATUS, "Status"),(DWORD, "Reserved"),(PFW_OBJECT_METADATA, "pMetaData"),]

    
PFW_MM_RULE = FW_MM_RULE
class FW_MATCH_VALUE(NdrStructure):
    MEMBERS = [(FW_DATA_TYPE, "type"),(U0, "u0"),]

    

class FW_QUERY_CONDITION(NdrStructure):
    MEMBERS = [(FW_MATCH_KEY, "matchKey"),(FW_MATCH_TYPE, "matchType"),(FW_MATCH_VALUE, "matchValue"),]

    
PFW_QUERY_CONDITION = FW_QUERY_CONDITION
class FW_QUERY_CONDITIONS(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(PFW_QUERY_CONDITION, "AndedConditions"),]

    
PFW_QUERY_CONDITIONS = FW_QUERY_CONDITIONS
class FW_QUERY(NdrStructure):
    MEMBERS = [(WORD, "wSchemaVersion"),(UINT32, "dwNumEntries"),(PFW_QUERY_CONDITIONS, "ORConditions"),(FW_RULE_STATUS, "Status"),]

    
PFW_QUERY = FW_QUERYMethod("RRPC_FWOpenPolicyStore",
In(FW_CONN_HANDLE),
In(WORD),
In(FW_STORE_TYPE),
In(FW_POLICY_ACCESS_RIGHT),
In(DWORD),
Out(PFW_POLICY_STORE_HANDLE),
),Method("RRPC_FWClosePolicyStore",
In(FW_CONN_HANDLE),
InOut(PFW_POLICY_STORE_HANDLE),
),Method("RRPC_FWRestoreDefaults",
In(FW_CONN_HANDLE),
),Method("RRPC_FWGetGlobalConfig",
In(FW_CONN_HANDLE),
In(WORD),
In(FW_STORE_TYPE),
In(FW_GLOBAL_CONFIG),
In(DWORD),
InOut(PBYTE),
In(DWORD),
InOut(LPDWORD),
Out(LPDWORD),
),Method("RRPC_FWSetGlobalConfig",
In(FW_CONN_HANDLE),
In(WORD),
In(FW_STORE_TYPE),
In(FW_GLOBAL_CONFIG),
In(PBYTE),
In(DWORD),
),Method("RRPC_FWAddFirewallRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_0),
),Method("RRPC_FWSetFirewallRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_0),
),Method("RRPC_FWDeleteFirewallRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(LPCWSTR),
),Method("RRPC_FWDeleteAllFirewallRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
),Method("RRPC_FWEnumFirewallRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_0),
),Method("RRPC_FWGetConfig",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_PROFILE_CONFIG),
In(FW_PROFILE_TYPE),
In(DWORD),
InOut(PBYTE),
In(DWORD),
InOut(LPDWORD),
Out(LPDWORD),
),Method("RRPC_FWSetConfig",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_PROFILE_CONFIG),
In(FW_PROFILE_TYPE),
In(FW_PROFILE_CONFIG_VALUE),
In(DWORD),
),Method("RRPC_FWAddConnectionSecurityRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CS_RULE2_0),
),Method("RRPC_FWSetConnectionSecurityRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CS_RULE2_0),
),Method("RRPC_FWDeleteConnectionSecurityRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(LPWSTR),
),Method("RRPC_FWDeleteAllConnectionSecurityRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
),Method("RRPC_FWEnumConnectionSecurityRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_CS_RULE2_0),
),Method("RRPC_FWAddAuthenticationSet",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_AUTH_SET2_10),
),Method("RRPC_FWSetAuthenticationSet",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_AUTH_SET2_10),
),Method("RRPC_FWDeleteAuthenticationSet",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(LPCWSTR),
),Method("RRPC_FWDeleteAllAuthenticationSets",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
),Method("RRPC_FWEnumAuthenticationSets",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_AUTH_SET2_10),
),Method("RRPC_FWAddCryptoSet",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CRYPTO_SET),
),Method("RRPC_FWSetCryptoSet",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CRYPTO_SET),
),Method("RRPC_FWDeleteCryptoSet",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(LPCWSTR),
),Method("RRPC_FWDeleteAllCryptoSets",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
),Method("RRPC_FWEnumCryptoSets",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_CRYPTO_SET),
),Method("RRPC_FWEnumPhase1SAs",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_ENDPOINTS),
Out(PDWORD),
Out(PPFW_PHASE1_SA_DETAILS),
),Method("RRPC_FWEnumPhase2SAs",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_ENDPOINTS),
Out(PDWORD),
Out(PPFW_PHASE2_SA_DETAILS),
),Method("RRPC_FWDeletePhase1SAs",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_ENDPOINTS),
),Method("RRPC_FWDeletePhase2SAs",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_ENDPOINTS),
),Method("RRPC_FWEnumProducts",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
Out(PDWORD),
Out(PPFW_PRODUCT),
),Method("RRPC_FWAddMainModeRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_MM_RULE),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetMainModeRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_MM_RULE),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWDeleteMainModeRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(LPWSTR),
),Method("RRPC_FWDeleteAllMainModeRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
),Method("RRPC_FWEnumMainModeRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_MM_RULE),
),Method("RRPC_FWQueryFirewallRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_10),
),Method("RRPC_FWQueryConnectionSecurityRules2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_CS_RULE2_10),
),Method("RRPC_FWQueryMainModeRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_MM_RULE),
),Method("RRPC_FWQueryAuthenticationSets",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_AUTH_SET2_10),
),Method("RRPC_FWQueryCryptoSets",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_CRYPTO_SET),
),Method("RRPC_FWEnumNetworks",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
Out(PDWORD),
Out(PPFW_NETWORK),
),Method("RRPC_FWEnumAdapters",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
Out(PDWORD),
Out(PPFW_ADAPTER),
),Method("RRPC_FWGetGlobalConfig2_10",
In(FW_CONN_HANDLE),
In(WORD),
In(FW_STORE_TYPE),
In(FW_GLOBAL_CONFIG),
In(DWORD),
InOut(PBYTE),
In(DWORD),
InOut(LPDWORD),
Out(LPDWORD),
Out(PFW_RULE_ORIGIN_TYPE),
),Method("RRPC_FWGetConfig2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_PROFILE_CONFIG),
In(FW_PROFILE_TYPE),
In(DWORD),
InOut(PBYTE),
In(DWORD),
InOut(LPDWORD),
Out(LPDWORD),
Out(PFW_RULE_ORIGIN_TYPE),
),Method("RRPC_FWAddFirewallRule2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_10),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_10),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_10),
),Method("RRPC_FWAddConnectionSecurityRule2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CS_RULE2_10),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetConnectionSecurityRule2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CS_RULE2_10),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumConnectionSecurityRules2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_CS_RULE2_10),
),Method("RRPC_FWAddAuthenticationSet2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_AUTH_SET2_10),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetAuthenticationSet2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_AUTH_SET2_10),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumAuthenticationSets2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_AUTH_SET2_10),
),Method("RRPC_FWAddCryptoSet2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CRYPTO_SET),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetCryptoSet2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CRYPTO_SET),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumCryptoSets2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_CRYPTO_SET),
),Method("RRPC_FWAddConnectionSecurityRule2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CS_RULE),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetConnectionSecurityRule2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CS_RULE),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumConnectionSecurityRules2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_CS_RULE),
),Method("RRPC_FWQueryConnectionSecurityRules2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_CS_RULE),
),Method("RRPC_FWAddAuthenticationSet2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_AUTH_SET),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetAuthenticationSet2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_AUTH_SET),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumAuthenticationSets2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_AUTH_SET),
),Method("RRPC_FWQueryAuthenticationSets2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_AUTH_SET),
),Method("RRPC_FWAddFirewallRule2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_20),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_20),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_20),
),Method("RRPC_FWQueryFirewallRules2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_20),
),Method("RRPC_FWAddFirewallRule2_24",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_24),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_24",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_24),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_24",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_24),
),Method("RRPC_FWQueryFirewallRules2_24",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_24),
),Method("RRPC_FWAddFirewallRule2_25",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_25),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_25",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_25),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_25",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_25),
),Method("RRPC_FWQueryFirewallRules2_25",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_25),
),Method("RRPC_FWAddFirewallRule2_26",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_26),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_26",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_26),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_26",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_26),
),Method("RRPC_FWQueryFirewallRules2_26",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_26),
),Method("RRPC_FWAddFirewallRule2_27",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_27),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_27",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_27),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_27",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_27),
),Method("RRPC_FWQueryFirewallRules2_27",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_27),
),Method("RRPC_FWAddFirewallRule2_31",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_31",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_31",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE),
),Method("RRPC_FWQueryFirewallRules2_31",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE),
),