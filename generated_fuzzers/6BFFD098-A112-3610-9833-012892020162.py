from fuzzer.midl import *
from fuzzer.core import *

Method("Opnum0NotUsedOnWire", In(),), Method("Opnum1NotUsedOnWire", In(),), Method(
    "I_BrowserrQueryOtherDomains",
    In(BROWSER_IDENTIFY_HANDLE),
    InOut(LPSERVER_ENUM_STRUCT),
    Out(LPDWORD),
), Method("Opnum3NotUsedOnWire", In(),), Method("Opnum4NotUsedOnWire", In(),), Method(
    "Opnum5NotUsedOnWire",
    In(),
), Method(
    "Opnum6NotUsedOnWire",
    In(),
), Method(
    "Opnum7NotUsedOnWire",
    In(),
), Method(
    "Opnum8NotUsedOnWire",
    In(),
), Method(
    "Opnum9NotUsedOnWire",
    In(),
), Method(
    "Opnum10NotUsedOnWire",
    In(),
), Method(
    "Opnum11NotUsedOnWire",
    In(),
),
