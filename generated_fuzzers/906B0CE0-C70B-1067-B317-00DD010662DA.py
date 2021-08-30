
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("906B0CE0-C70B-1067-B317-00DD010662DA", "1.0",[
Method("Poke",
In(HANDLE_T),
In(SESSION_RANK),
In(UNSIGNED_CHAR),
In(UNSIGNED_CHAR),
In(UNSIGNED_CHAR),
In(DWORD),
In(UNSIGNED_CHAR),
),
Method("BuildContext",
In(HANDLE_T),
In(SESSION_RANK),
In(BIND_VERSION_SET),
In(UNSIGNED_CHAR),
In(UNSIGNED_CHAR),
In(UNSIGNED_CHAR),
In(UNSIGNED_CHAR),
InOut(UNSIGNED_CHAR),
InOut(PBOUND_VERSION_SET),
In(DWORD),
In(UNSIGNED_CHAR),
Out(PPCONTEXT_HANDLE),
),
Method("NegotiateResources",
In(PCONTEXT_HANDLE),
In(RESOURCE_TYPE),
In(DWORD),
InOut(PDWORD),
),
Method("SendReceive",
In(PCONTEXT_HANDLE),
In(DWORD),
In(DWORD),
In(UNSIGNED_CHAR),
),
Method("TearDownContext",
InOut(PPCONTEXT_HANDLE),
In(SESSION_RANK),
In(TEARDOWN_TYPE),
),
Method("BeginTearDown",
In(PCONTEXT_HANDLE),
In(TEARDOWN_TYPE),
),
Method("PokeW",
In(HANDLE_T),
In(SESSION_RANK),
In(WCHAR_T),
In(WCHAR_T),
In(WCHAR_T),
In(DWORD),
In(UNSIGNED_CHAR),
),
Method("BuildContextW",
In(HANDLE_T),
In(SESSION_RANK),
In(BIND_VERSION_SET),
In(WCHAR_T),
In(WCHAR_T),
In(WCHAR_T),
In(WCHAR_T),
InOut(WCHAR_T),
InOut(PBOUND_VERSION_SET),
In(DWORD),
In(UNSIGNED_CHAR),
Out(PPCONTEXT_HANDLE),
),
])
