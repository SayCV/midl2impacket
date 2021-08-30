
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("FA7DF749-667-4986-A27F-E2F04AE53772", "1.0",[
Method("GetProviderMgmtInterface",
In(VSS_ID),
In(REFIID),
Out(PPIUNKNOWN),
),
Method("QueryVolumesSupportedForSnapshots",
In(VSS_ID),
In(LONG),
Out(PPIVSSENUMMGMTOBJECT),
),
Method("QuerySnapshotsByVolume",
In(VSS_PWSZ),
In(VSS_ID),
Out(PPIVSSENUMOBJECT),
),
])
interface_1 = Interface("214A0F28-B737-4026-B847-4F9E37D79529", "1.0",[
Method("AddDiffArea",
In(VSS_PWSZ),
In(VSS_PWSZ),
In(LONGLONG),
),
Method("ChangeDiffAreaMaximumSize",
In(VSS_PWSZ),
In(VSS_PWSZ),
In(LONGLONG),
),
Method("QueryVolumesSupportedForDiffAreas",
In(VSS_PWSZ),
Out(PPIVSSENUMMGMTOBJECT),
),
Method("QueryDiffAreasForVolume",
In(VSS_PWSZ),
Out(PPIVSSENUMMGMTOBJECT),
),
Method("QueryDiffAreasOnVolume",
In(VSS_PWSZ),
Out(PPIVSSENUMMGMTOBJECT),
),
Method("Opnum08NotUsedOnWire",
In(),
),
])
interface_2 = Interface("AE1C7110-260-113-839-00047283", "1.0",[
Method("Next",
In(ULONG),
Out(PVSS_OBJECT_PROP),
Out(PULONG),
),
Method("Skip",
In(ULONG),
),
Method("Reset",
),
Method("Clone",
InOut(PPIVSSENUMOBJECT),
),
])
interface_3 = Interface("01954E6B-9254-4e6e-808C-C9E05D007696", "1.0",[
Method("Next",
In(ULONG),
Out(PVSS_MGMT_OBJECT_PROP),
Out(PULONG),
),
Method("Skip",
In(ULONG),
),
Method("Reset",
),
Method("Clone",
InOut(PPIVSSENUMMGMTOBJECT),
),
])
