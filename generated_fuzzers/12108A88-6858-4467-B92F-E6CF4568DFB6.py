
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("12108A88-6858-4467-B92F-E6CF4568DFB6", "1.0",[
Method("CprepDiskRawRead",
In(CPREP_DISKID),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
Out(PBYTE),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),
Method("CprepDiskRawWrite",
In(CPREP_DISKID),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(PBYTE),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),
Method("CprepPrepareNode",
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),
Method("CprepPrepareNodePhase2",
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),
Method("CprepDiskGetProps",
In(CPREP_DISKID),
Out(PDISK_PROPS),
),
Method("Opnum8NotUsedOnWire",
),
Method("Opnum9NotUsedOnWire",
),
Method("Opnum10NotUsedOnWire",
),
Method("Opnum11NotUsedOnWire",
),
Method("CprepDiskStopDefense",
In(CPREP_DISKID),
),
Method("CprepDiskOnline",
In(CPREP_DISKID),
Out(PUNSIGNED_LONG),
),
Method("CprepDiskVerifyUnique",
In(CPREP_DISKID),
),
Method("Opnum15NotUsedOnWire",
),
Method("Opnum16NotUsedOnWire",
),
Method("CprepDiskWriteFileData",
In(CPREP_DISKID),
In(UNSIGNED_LONG),
In(PWCHAR_T),
In(UNSIGNED_LONG),
In(PBYTE),
),
Method("CprepDiskVerifyFileData",
In(CPREP_DISKID),
In(UNSIGNED_LONG),
In(PWCHAR_T),
In(UNSIGNED_LONG),
In(PBYTE),
),
Method("CprepDiskDeleteFile",
In(CPREP_DISKID),
In(UNSIGNED_LONG),
In(PWCHAR_T),
),
Method("CprepDiskOffline",
In(CPREP_DISKID),
),
Method("Opnum21NotUsedOnWire",
),
Method("CprepDiskGetUniqueIds",
In(CPREP_DISKID),
In(UNSIGNED_LONG),
Out(PBYTE),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),
Method("CprepDiskAttach",
In(CPREP_DISKID),
),
Method("CprepDiskPRArbitrate",
In(CPREP_DISKID),
),
Method("CprepDiskPRRegister",
In(CPREP_DISKID),
),
Method("CprepDiskPRUnRegister",
In(CPREP_DISKID),
),
Method("CprepDiskPRReserve",
In(CPREP_DISKID),
),
Method("CprepDiskPRRelease",
In(CPREP_DISKID),
),
Method("CprepDiskDiskPartitionIsNtfs",
In(CPREP_DISKID),
In(UNSIGNED_LONG),
),
Method("CprepDiskGetArbSectors",
In(CPREP_DISKID),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),
Method("CprepDiskIsPRPresent",
In(CPREP_DISKID),
Out(PUNSIGNED_LONG),
),
Method("CprepDiskPRPreempt",
In(CPREP_DISKID),
),
Method("CprepDiskPRClear",
In(CPREP_DISKID),
),
Method("CprepDiskIsOnline",
In(CPREP_DISKID),
),
Method("CprepDiskSetOnline",
In(CPREP_DISKID),
),
Method("CprepDiskGetFSName",
In(CPREP_DISKID),
In(UNSIGNED_LONG),
Out(WCHAR_T),
),
Method("CprepDiskIsReadable",
In(CPREP_DISKID),
),
Method("CprepDiskGetDsms",
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PBYTE),
),
])
interface_1 = Interface("11942D87-A1DE-4E7F-83FB-A840D9C5928D", "1.0",[
Method("CprepDiskGetUniqueIds3",
In(CPREP_DISKID),
Out(PPBYTE),
Out(PULONG),
Out(PPBYTE),
Out(PULONG),
),
Method("CprepCheckNetFtBindings3",
In(),
),
Method("CprepCsvTestSetup3",
In(GUID),
In(LPWSTR),
),
Method("CprepIsNodeClustered3",
Out(PBOOLEAN),
),
Method("CprepCreateNewSmbShares3",
Out(PPLPWSTR),
Out(PDWORD),
),
Method("CprepConnectToNewSmbShares3",
In(PLPWSTR),
In(DWORD),
),
Method("CprepDiskGetProps3",
In(CPREP_DISKID),
Out(PDISK_PROPS_EX),
),
Method("CprepDiskIsReadOnly3",
In(CPREP_DISKID),
Out(PBOOLEAN),
),
Method("CprepDiskPRRegister3",
In(CPREP_DISKID),
In(ULONGLONG),
In(ULONGLONG),
),
Method("CprepDiskFindKey3",
In(CPREP_DISKID),
In(ULONGLONG),
Out(PBOOLEAN),
),
Method("CprepDiskPRPreempt3",
In(CPREP_DISKID),
In(ULONGLONG),
In(ULONGLONG),
),
Method("CprepDiskPRReserve3",
In(CPREP_DISKID),
In(ULONGLONG),
),
Method("CprepDiskIsPRPresent3",
In(CPREP_DISKID),
In(ULONGLONG),
),
Method("CprepDiskPRRelease3",
In(CPREP_DISKID),
In(ULONGLONG),
),
Method("CprepDiskPRClear3",
In(CPREP_DISKID),
In(ULONGLONG),
),
])
interface_2 = Interface("2931C32C-F731-4c56-9FEB-3D5F1C5E72BF", "1.0",[
Method("SendRTMessage",
In(BSTR),
In(BSTR),
In(UNSIGNED_SHORT),
In(UNSIGNED_SHORT),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),
Method("InitializeNode",
In(UNSIGNED_SHORT),
Out(PUNSIGNED_SHORT),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),
Method("GetIpConfigSerialized",
In(BOOLEAN),
Out(PSAFEARRAY),
Out(PINT),
),
Method("CleanupNode",
),
Method("QueryFirewallConfiguration",
Out(PBOOLEAN),
Out(PBOOLEAN),
),
Method("ProcessAddRoutes",
In(PADD_ROUTES_REQUEST),
),
Method("GetAddRoutesStatus",
Out(PADD_ROUTES_REPLY),
),
Method("Opnum10Reserved",
),
Method("CancelAddRoutesRequest",
),
])
interface_3 = Interface("D6105110-8917-415-AA32-80A2933DC9", "1.0",[
Method("CleanUpEvictedNode",
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
),
Method("ClearPR",
In(UNSIGNED_LONG),
),
])
interface_4 = Interface("491260B5-05C9-40D9-B7F2-1F7BDAE0927F", "1.0",[
Method("ConfigSvcSecret",
In(BSTR),
),
Method("RetrieveSvcSecret",
Out(PBSTR),
),
Method("RetrieveHostLabel",
Out(PBSTR),
),
Method("GetFunctionalLevel",
Out(PWORD),
),
Method("Opnum7Reserved",
),
Method("Opnum8Reserved",
),
Method("ConfigClusterCert",
In(PCLUSTER_CERT),
),
Method("RetrieveClusterCert",
Out(PCLUSTER_CERT),
),
Method("GenerateClusterCert",
InOut(PCLUSTER_CERT),
),
Method("GetUpgradeVersion",
Out(PWORD),
),
Method("Opnum13Reserved",
),
Method("ConfigClusterCerV2",
In(PCLUSTER_CERT),
In(CLUSTER_CERTTYPE),
),
Method("RetrieveClusterCertV2",
In(PCLUSTER_CERT),
Out(PCLUSTER_CERTTYPE),
),
Method("GenerateClusterCertV2",
InOut(PCLUSTER_CERT),
In(CLUSTER_CERTTYPE),
),
])
interface_5 = Interface("85923CA7-1B6B-4E83-A2E4-F5BA3BFBB8A3", "1.0",[
Method("GenerateClusterLog",
Out(PBSTR),
),
Method("GenerateTimeSpanLog",
In(UNSIGNED_LONG),
Out(PBSTR),
),
Method("GenerateClusterLogInLocalTime",
Out(PBSTR),
),
Method("GenerateTimeSpanLogInLocalTime",
In(ULONG),
Out(PBSTR),
),
])
interface_6 = Interface("BD7C23C2-C805-457-886-D17FE6B9D19F", "1.0",[
Method("GenerateClusterLog",
In(ULONG),
In(CLUSTERLOGEXFLAG),
Out(PBSTR),
),
Method("GenerateClusterHealthLog",
In(ULONG),
In(CLUSTERLOGEXFLAG),
Out(PBSTR),
),
])
interface_7 = Interface("F1D6C29C-8BE-4691-8724-F6D8DEAEAFC8", "1.0",[
Method("InitializeAdapterConfiguration",
Out(PUNSIGNED_LONG),
),
Method("GetNextAdapterFirewallConfiguration",
In(UNSIGNED_LONG),
Out(PGUID),
Out(PCLUSTER_NETWORK_PROFILE),
Out(PBOOLEAN),
Out(PBOOLEAN),
Out(PBOOLEAN),
),
])
interface_8 = Interface("E3C9B851-C442-432-8C6-A7FAAFC09D3B", "1.0",[
Method("GetUpdates",
Out(PULONG),
Out(PBSTR),
),
Method("Count",
Out(PLONG),
),
])
