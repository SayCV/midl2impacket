from .base import Converter
from .struct import MidlStructConverter
from .procedure import MidlProcedureConverter
from midl import (
    MidlInterface,
    MidlTypeDef,
    MidlSimpleTypedef,
    MidlStructDef,
    MidlUnionDef,
    MidlEnumDef,
    MidlVarDef,
)
from impacketbuilder.ndrbuilder.python import (
    PythonAssignment,
    PythonDictEntry,
    PythonDictEntryList,
    PythonDict,
    PythonValue,
    PythonName,
    PythonTuple,
)

from impacketbuilder.ndrbuilder.ndr import PythonNdrStruct, PythonNdrPointer


class MidlInterfaceConverter(Converter):
    def convert(self, interface):
        # write uuid def
        self.uuid(interface)
        for vd in interface.vardefs:
            self.handle_vardef(vd)
        for td in interface.typedefs:
            self.handle_typedef(td)
        count = 0
        mapping = {}
        for proc in interface.procedures:
            self.handle_procedure(proc, count)
            mapping[proc.name] = proc.name + "Response"
            count += 1

        dentries = []
        count = 0
        for k in mapping:
            dentries.append(PythonDictEntry(
                PythonValue(count),
                PythonTuple([PythonValue(k), PythonValue(mapping[k])]),
            ))
            count += 1

        rhs = PythonDict(PythonDictEntryList(*dentries))
        opnum_map = PythonAssignment(PythonName("OPNUMS"), rhs)

        self.write(opnum_map)

    def uuid(self, interface: MidlInterface):
        int_name = f"MSRPC_UUID_{interface.name.upper()}"
        if "uuid" in interface.attributes.keys():
            self.write(
                PythonAssignment(
                    PythonValue(int_name),
                    PythonValue(
                        f"uuidtup_to_bin(('{interface.attributes['uuid'].params[0]}','0.0'))"
                    ),
                )
            )

    def handle_procedure(self, proc, count):
        MidlProcedureConverter(self.io, self.tab_level, mapper=self.mapper).convert(
            proc, count
        )

    def handle_typedef(self, td):
        if type(td) is MidlTypeDef:
            self.handle_midl_td(td)
        elif type(td) in [MidlStructDef, MidlUnionDef]:
            self.handle_midl_struct(td)
        elif type(td) is MidlEnumDef:
            self.handle_midl_enum(td)
        elif type(td) is MidlSimpleTypedef:
            self.handle_midl_td(td)
        else:
            raise Exception(
                f"MidlInterfaceConverter: Unhandled typedef type: {td.__class__}"
            )

    def handle_vardef(self, vd: MidlVarDef):
        self.write(f"{vd.name} = {self.mapper.canonicalize(vd.type)}")

    def handle_midl_td(self, td: MidlTypeDef):
        if type(td) is MidlTypeDef:
            attr_names = [td.attributes[k].name for k in td.attributes.keys()]
            if "context_handle" in attr_names:
                self.handle_context_handle(td)
            else:
                print(":asdDadssd")
        elif type(td) is MidlSimpleTypedef:
            self.write(
                PythonAssignment(
                    PythonValue(self.mapper.canonicalize(td.name)),
                    PythonValue(self.mapper.canonicalize(td.type)),
                )
            )

    def handle_context_handle(self, td):
        pointer_name = td.name
        real_name = td.name
        if td.name[0] == "P":
            real_name = td.name[1:]

        structure = PythonTuple(
            PythonTuple([PythonValue("'Data'"), PythonValue("'20s=\"\"'")])
        )
        ndr_struct = PythonNdrStruct(name=real_name, structure=structure)
        self.write(ndr_struct.to_string())

        ndr_pointer = PythonNdrPointer(name=pointer_name, referent_name=real_name)
        self.write(ndr_pointer.to_string())

    def handle_midl_struct(self, td: MidlStructDef):
        struct_converter = MidlStructConverter(
            self.io, self.tab_level, mapper=self.mapper
        )
        struct_converter.convert(td)

    def handle_midl_enum(self, td: MidlEnumDef):
        self.write(PythonAssignment(PythonName(td.public_names[0]),PythonValue("DWORD__ENUM")))
        val = td.map[list(td.map.keys())[0]]
        if val == None:
            # default enum value case
            value = 0
            for key in td.map.keys():
                td.map[key] = value
                value+=1

        for key in td.map.keys():
            val = td.map[key]
            enum = PythonAssignment(PythonName(key), PythonValue(str(val)))
            self.write(enum)
