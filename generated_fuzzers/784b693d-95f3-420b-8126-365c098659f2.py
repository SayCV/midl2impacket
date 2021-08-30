
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("784b693d-95f3-420b-8126-365c098659f2", "1.0",[
Method("GetOCSPProperty",
In(BSTR),
Out(PVARIANT),
),
Method("SetOCSPProperty",
In(BSTR),
In(PVARIANT),
),
Method("GetCAConfigInformation",
In(BSTR),
Out(PVARIANT),
),
Method("SetCAConfigInformation",
In(BSTR),
In(PVARIANT),
),
Method("GetSecurity",
Out(PCERTTRANSBLOB),
),
Method("SetSecurity",
In(PCERTTRANSBLOB),
),
Method("GetSigningCertificates",
In(PVARIANT),
Out(PVARIANT),
),
Method("GetHashAlgorithms",
In(BSTR),
Out(PVARIANT),
),
Method("GetMyRoles",
Out(PLONG),
),
Method("Ping",
),
])
