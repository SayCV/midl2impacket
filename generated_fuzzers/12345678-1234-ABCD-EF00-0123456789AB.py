from fuzzer.midl import *
from fuzzer.core import *

Method(
    "RpcEnumPrinters",
    In(DWORD),
    In(STRING_HANDLE),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "RpcOpenPrinter",
    In(STRING_HANDLE),
    Out(PPRINTER_HANDLE),
    In(PWCHAR_T),
    In(PDEVMODE_CONTAINER),
    In(DWORD),
), Method(
    "RpcSetJob",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(PJOB_CONTAINER),
    In(DWORD),
), Method(
    "RpcGetJob",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcEnumJobs",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(DWORD),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "RpcAddPrinter",
    In(STRING_HANDLE),
    In(PPRINTER_CONTAINER),
    In(PDEVMODE_CONTAINER),
    In(PSECURITY_CONTAINER),
    Out(PPRINTER_HANDLE),
), Method(
    "RpcDeletePrinter",
    In(PRINTER_HANDLE),
), Method(
    "RpcSetPrinter",
    In(PRINTER_HANDLE),
    In(PPRINTER_CONTAINER),
    In(PDEVMODE_CONTAINER),
    In(PSECURITY_CONTAINER),
    In(DWORD),
), Method(
    "RpcGetPrinter",
    In(PRINTER_HANDLE),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcAddPrinterDriver",
    In(STRING_HANDLE),
    In(PDRIVER_CONTAINER),
), Method(
    "RpcEnumPrinterDrivers",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "RpcGetPrinterDriver",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcGetPrinterDriverDirectory",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcDeletePrinterDriver",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
), Method(
    "RpcAddPrintProcessor",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
    In(PWCHAR_T),
), Method(
    "RpcEnumPrintProcessors",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "RpcGetPrintProcessorDirectory",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcStartDocPrinter",
    In(PRINTER_HANDLE),
    In(PDOC_INFO_CONTAINER),
    Out(PDWORD),
), Method(
    "RpcStartPagePrinter",
    In(PRINTER_HANDLE),
), Method(
    "RpcWritePrinter",
    In(PRINTER_HANDLE),
    In(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcEndPagePrinter",
    In(PRINTER_HANDLE),
), Method(
    "RpcAbortPrinter",
    In(PRINTER_HANDLE),
), Method(
    "RpcReadPrinter",
    In(PRINTER_HANDLE),
    Out(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcEndDocPrinter",
    In(PRINTER_HANDLE),
), Method(
    "RpcAddJob",
    In(PRINTER_HANDLE),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcScheduleJob",
    In(PRINTER_HANDLE),
    In(DWORD),
), Method(
    "RpcGetPrinterData",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    Out(PDWORD),
    Out(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcSetPrinterData",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    In(DWORD),
    In(PBYTE),
    In(DWORD),
), Method(
    "RpcWaitForPrinterChange",
    In(PRINTER_HANDLE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcClosePrinter",
    InOut(PPRINTER_HANDLE),
), Method(
    "RpcAddForm",
    In(PRINTER_HANDLE),
    In(PFORM_CONTAINER),
), Method(
    "RpcDeleteForm",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
), Method(
    "RpcGetForm",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcSetForm",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    In(PFORM_CONTAINER),
), Method(
    "RpcEnumForms",
    In(PRINTER_HANDLE),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "RpcEnumPorts",
    In(STRING_HANDLE),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "RpcEnumMonitors",
    In(STRING_HANDLE),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "Opnum37NotUsedOnWire",
), Method(
    "Opnum38NotUsedOnWire",
), Method(
    "RpcDeletePort",
    In(STRING_HANDLE),
    In(ULONG_PTR),
    In(PWCHAR_T),
), Method(
    "RpcCreatePrinterIC",
    In(PRINTER_HANDLE),
    Out(PGDI_HANDLE),
    In(PDEVMODE_CONTAINER),
), Method(
    "RpcPlayGdiScriptOnPrinterIC",
    In(GDI_HANDLE),
    In(PBYTE),
    In(DWORD),
    Out(PBYTE),
    In(DWORD),
    In(DWORD),
), Method(
    "RpcDeletePrinterIC",
    InOut(PGDI_HANDLE),
), Method(
    "Opnum43NotUsedOnWire",
), Method(
    "Opnum44NotUsedOnWire",
), Method(
    "Opnum45NotUsedOnWire",
), Method(
    "RpcAddMonitor",
    In(STRING_HANDLE),
    In(PMONITOR_CONTAINER),
), Method(
    "RpcDeleteMonitor",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
), Method(
    "RpcDeletePrintProcessor",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
), Method(
    "Opnum49NotUsedOnWire",
), Method(
    "Opnum50NotUsedOnWire",
), Method(
    "RpcEnumPrintProcessorDatatypes",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "RpcResetPrinter",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    In(PDEVMODE_CONTAINER),
), Method(
    "RpcGetPrinterDriver2",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    In(DWORD),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
    In(DWORD),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "Opnum54NotUsedOnWire",
), Method(
    "Opnum55NotUsedOnWire",
), Method(
    "RpcFindClosePrinterChangeNotification",
    In(PRINTER_HANDLE),
), Method(
    "Opnum57NotUsedOnWire",
), Method(
    "RpcReplyOpenPrinter",
    In(STRING_HANDLE),
    Out(PPRINTER_HANDLE),
    In(DWORD),
    In(DWORD),
    In(DWORD),
    In(PBYTE),
), Method(
    "RpcRouterReplyPrinter",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(DWORD),
    In(PBYTE),
), Method(
    "RpcReplyClosePrinter",
    InOut(PPRINTER_HANDLE),
), Method(
    "RpcAddPortEx",
    In(STRING_HANDLE),
    In(PPORT_CONTAINER),
    In(PPORT_VAR_CONTAINER),
    In(PWCHAR_T),
), Method(
    "RpcRemoteFindFirstPrinterChangeNotification",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(DWORD),
    In(PWCHAR_T),
    In(DWORD),
    In(DWORD),
    InOut(PBYTE),
), Method(
    "Opnum63NotUsedOnWire",
), Method(
    "Opnum64NotUsedOnWire",
), Method(
    "RpcRemoteFindFirstPrinterChangeNotificationEx",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(DWORD),
    In(PWCHAR_T),
    In(DWORD),
    In(PRPC_V2_NOTIFY_OPTIONS),
), Method(
    "RpcRouterReplyPrinterEx",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(DWORD),
    Out(PDWORD),
    In(DWORD),
    In(RPC_V2_UREPLY_PRINTER),
), Method(
    "RpcRouterRefreshPrinterChangeNotification",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(PRPC_V2_NOTIFY_OPTIONS),
    Out(PPRPC_V2_NOTIFY_INFO),
), Method(
    "Opnum68NotUsedOnWire",
), Method(
    "RpcOpenPrinterEx",
    In(STRING_HANDLE),
    Out(PPRINTER_HANDLE),
    In(PWCHAR_T),
    In(PDEVMODE_CONTAINER),
    In(DWORD),
    In(PSPLCLIENT_CONTAINER),
), Method(
    "RpcAddPrinterEx",
    In(STRING_HANDLE),
    In(PPRINTER_CONTAINER),
    In(PDEVMODE_CONTAINER),
    In(PSECURITY_CONTAINER),
    In(PSPLCLIENT_CONTAINER),
    Out(PPRINTER_HANDLE),
), Method(
    "RpcSetPort",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(PPORT_CONTAINER),
), Method(
    "RpcEnumPrinterData",
    In(PRINTER_HANDLE),
    In(DWORD),
    Out(PWCHAR_T),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
    Out(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcDeletePrinterData",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
), Method(
    "Opnum74NotUsedOnWire",
), Method(
    "Opnum75NotUsedOnWire",
), Method(
    "Opnum76NotUsedOnWire",
), Method(
    "RpcSetPrinterDataEx",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
    In(DWORD),
    In(PBYTE),
    In(DWORD),
), Method(
    "RpcGetPrinterDataEx",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
    Out(PDWORD),
    Out(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcEnumPrinterDataEx",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    Out(PBYTE),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "RpcEnumPrinterKey",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    Out(PWCHAR_T),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RpcDeletePrinterDataEx",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
), Method(
    "RpcDeletePrinterKey",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
), Method(
    "Opnum83NotUsedOnWire",
), Method(
    "RpcDeletePrinterDriverEx",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
    In(DWORD),
    In(DWORD),
), Method(
    "RpcAddPerMachineConnection",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
    In(PWCHAR_T),
), Method(
    "RpcDeletePerMachineConnection",
    In(STRING_HANDLE),
    In(PWCHAR_T),
), Method(
    "RpcEnumPerMachineConnections",
    In(STRING_HANDLE),
    InOut(PBYTE),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "RpcXcvData",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    In(PBYTE),
    In(DWORD),
    Out(PBYTE),
    In(DWORD),
    Out(PDWORD),
    InOut(PDWORD),
), Method(
    "RpcAddPrinterDriverEx",
    In(STRING_HANDLE),
    In(PDRIVER_CONTAINER),
    In(DWORD),
), Method(
    "Opnum90NotUsedOnWire",
), Method(
    "Opnum91NotUsedOnWire",
), Method(
    "Opnum92NotUsedOnWire",
), Method(
    "Opnum93NotUsedOnWire",
), Method(
    "Opnum94NotUsedOnWire",
), Method(
    "Opnum95NotUsedOnWire",
), Method(
    "RpcFlushPrinter",
    In(PRINTER_HANDLE),
    In(PBYTE),
    In(DWORD),
    Out(PDWORD),
    In(DWORD),
), Method(
    "RpcSendRecvBidiData",
    In(PRINTER_HANDLE),
    In(PWCHAR_T),
    In(PRPC_BIDI_REQUEST_CONTAINER),
    Out(PPRPC_BIDI_RESPONSE_CONTAINER),
), Method(
    "Opnum98NotUsedOnWire",
), Method(
    "Opnum99NotUsedOnWire",
), Method(
    "Opnum100NotUsedOnWire",
), Method(
    "Opnum101NotUsedOnWire",
), Method(
    "RpcGetCorePrinterDrivers",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(DWORD),
    In(PWCHAR_T),
    In(DWORD),
    Out(PCORE_PRINTER_DRIVER),
), Method(
    "Opnum103NotUsedOnWire",
), Method(
    "RpcGetPrinterDriverPackagePath",
    In(STRING_HANDLE),
    In(PWCHAR_T),
    In(PWCHAR_T),
    In(PWCHAR_T),
    InOut(PWCHAR_T),
    In(DWORD),
    Out(LPDWORD),
), Method(
    "Opnum105NotUsedOnWire",
), Method(
    "Opnum106NotUsedOnWire",
), Method(
    "Opnum107NotUsedOnWire",
), Method(
    "Opnum108NotUsedOnWire",
), Method(
    "Opnum109NotUsedOnWire",
), Method(
    "RpcGetJobNamedPropertyValue",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(PWCHAR_T),
    Out(PRPC_PRINTPROPERTYVALUE),
), Method(
    "RpcSetJobNamedProperty",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(PRPC_PRINTNAMEDPROPERTY),
), Method(
    "RpcDeleteJobNamedProperty",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(PWCHAR_T),
), Method(
    "RpcEnumJobNamedProperties",
    In(PRINTER_HANDLE),
    In(DWORD),
    Out(PDWORD),
    Out(PPRPC_PRINTNAMEDPROPERTY),
), Method(
    "Opnum114NotUsedOnWire",
), Method(
    "Opnum115NotUsedOnWire",
), Method(
    "RpcLogJobInfoForBranchOffice",
    In(PRINTER_HANDLE),
    In(PRPC_BRANCHOFFICEJOBDATACONTAINER),
), Method(
    "RpcRegeneratePrintDeviceCapabilities",
    In(PRINTER_HANDLE),
), Method(
    "Opnum118NotUsedOnWire",
), Method(
    "RpcIppCreateJobOnPrinter",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(PWCHAR_T),
    In(DWORD),
    In(PBYTE),
    Out(PDWORD),
    Out(PPBYTE),
), Method(
    "RpcIppGetJobAttributes",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(DWORD),
    In(PPWCHAR_T),
    Out(PDWORD),
    Out(PPBYTE),
), Method(
    "RpcIppSetJobAttributes",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(DWORD),
    In(PBYTE),
    Out(PDWORD),
    Out(PPBYTE),
), Method(
    "RpcIppGetPrinterAttributes",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(PPWCHAR_T),
    Out(PDWORD),
    Out(PPBYTE),
), Method(
    "RpcIppSetPrinterAttributes",
    In(PRINTER_HANDLE),
    In(DWORD),
    In(PBYTE),
    Out(PDWORD),
    Out(PPBYTE),
),
