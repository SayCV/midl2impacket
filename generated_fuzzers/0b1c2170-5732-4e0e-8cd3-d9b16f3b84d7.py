
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7", "0.0",[
Method("AuthzrFreeContext",
InOut(PAUTHZR_HANDLE),
),
Method("AuthzrInitializeContextFromSid",
In(HANDLE_T),
In(DWORD),
In(PRPC_SID),
In(PLARGE_INTEGER),
In(LUID),
Out(PAUTHZR_HANDLE),
),
Method("AuthzrInitializeCompoundContext",
In(AUTHZR_HANDLE),
In(AUTHZR_HANDLE),
Out(PAUTHZR_HANDLE),
),
Method("AuthzrAccessCheck",
In(AUTHZR_HANDLE),
In(DWORD),
In(PAUTHZR_ACCESS_REQUEST),
In(DWORD),
In(PSR_SD),
InOut(PAUTHZR_ACCESS_REPLY),
),
Method("AuthzGetInformationFromContext",
In(AUTHZR_HANDLE),
In(AUTHZ_CONTEXT_INFORMATION_CLASS),
Out(PPAUTHZR_CONTEXT_INFORMATION),
),
Method("AuthzrModifyClaims",
In(AUTHZR_HANDLE),
In(AUTHZ_CONTEXT_INFORMATION_CLASS),
In(DWORD),
In(PAUTHZ_SECURITY_ATTRIBUTE_OPERATION),
In(PAUTHZR_SECURITY_ATTRIBUTES_INFORMATION),
),
Method("AuthzrModifySids",
In(AUTHZR_HANDLE),
In(AUTHZ_CONTEXT_INFORMATION_CLASS),
In(DWORD),
In(PAUTHZ_SID_OPERATION),
In(PAUTHZR_TOKEN_GROUPS),
),
])
