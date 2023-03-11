import pathlib
from io import StringIO

from midl2impacket.impacketbuilder.converters.typing import TypeMapper
from midl2impacket.midlparser import parse_idl
from midl2impacket.midltypes import (MidlDefinition, MidlEnumDef,
                                     MidlSimpleTypedef, MidlStructDef,
                                     MidlUnionDef)

from .datatype import IDL_TO_NDR


class FuzzerTemplateGenerator:
    """A class that generates fuzzing templates"""

    def __init__(self):
        self.io = StringIO()
        self.generated_classes = {}
        self.mapper = TypeMapper(None)
        self.static_imports = """
from midl2impacket.fuzzer.midl import *
from midl2impacket.fuzzer.core import *
"""
    def gen_class(self,name, members):
        clz = f"""
class {self.mapper.canonicalize(name)[0]}(NdrStructure):
    MEMBERS = [{members}]
"""
        self.io.write(clz)

    def static(self):
        if self.static_imports == "":
            return
        mapping = ""
        for idl_name, py_name in IDL_TO_NDR.items():
            canonicalized_name, _ = self.mapper.canonicalize(idl_name)
            if canonicalized_name != py_name:
                mapping += f"{canonicalized_name} = {py_name}\n"
            self.mapper.add_type(canonicalized_name)
        self.io.write(mapping)
        #Generate some impacket built in types, these are all implemented in the RPC runtime...
        self.gen_class("FILETIME", "(DWORD,'dwLowDateTime'),(LONG,'dwHighDateTime')")
        self.gen_class("LUID", "(DWORD,'LowPart'),(LONG,'HighPart')")
        self.gen_class("SYSTEMTIME", "(WORD,'wYear'),(WORD,'wMonth'),(WORD,'wDayOfWeek'),(WORD,'wDay'),(WORD,'wHour'),(WORD,'wMinute'),(WORD,'wSecond'),(WORD,'wMilliseconds'),")

    def generate_import(self, _import, import_dir):
        in_file = pathlib.Path(import_dir + _import.file)
        self.generate(parse_idl(in_file), import_dir)

    def generate(self, midl_def: MidlDefinition, import_dir):
        """Generates a Python file that is a fuzzing template"""
        # TODO handle imports
        self.io.write(self.static_imports)
        self.static()
        self.static_imports = ""
        for _import in midl_def.imports:
            self.generate_import(_import, import_dir)

        first_uuid = None
        # TODO generate struct defs first, before generating interface defs 
        for typedef in midl_def.typedefs:
            self.handle_typedef(typedef)
        for interface in midl_def.interfaces:
            if "uuid" in interface.attributes and first_uuid is None:
                first_uuid = interface.attributes["uuid"].params[0]
                self.generate_interface(interface)

        return self.io.getvalue(), first_uuid

    def handle_typedef(self, typedef):
        if isinstance(typedef, MidlUnionDef):
            self.generate_union(typedef)
        elif isinstance(typedef, MidlStructDef):
            self.generate_struct(typedef)
        elif isinstance(typedef, MidlEnumDef):
            self.generate_enum(typedef)
        elif isinstance(typedef, MidlSimpleTypedef):
            # TODO Add this typedef mapping to a type hierarchy lookup mapper
            self.io.write(f"{self.mapper.canonicalize(typedef.name)[0]} = {self.mapper.canonicalize(typedef.type.replace('*',''))[0]}\n")
        elif typedef is None:
            return ""
        else:
            raise Exception(f"Unhandled typedef {type(typedef)}")

    def generate_union(self, union: MidlUnionDef):
        output = ""
        # TODO add typedef mapping for all public names of this struct
        if len(union.public_names) > 0:
            name = union.public_names[0]
        else:
            name = union.private_name
        # TODO do a proper switch_type lookup
        switch_type = "DWORD"
        members = ""
        member_cnt = 1
        for member in union.members:
            type_name = member.type
            if isinstance(member.type, (MidlUnionDef, MidlStructDef)):
                # handle nested unions/structs
                self.handle_typedef(member.type)
                if len(member.type.public_names) > 0:
                    type_name = member.type.public_names[0]
                else:
                    type_name = member.type.private_name

            if isinstance(type_name, str):
                members += f'{member_cnt} : ({self.mapper.canonicalize(type_name)[0]}, "{member.name}"),'
            member_cnt += 1

        class_def = f"""
class {self.mapper.canonicalize(name)[0]}(NdrUnion):
    SWITCHTYPE = {switch_type}
    MEMBERS = {{{members}}}

    
"""
        self.io.write(class_def)
        for n in union.public_names:
            if n != name:
                n = n.replace("*","")
                #TODO still need to generate code to add this to the type alias lookup at runtime
                self.io.write(f"{self.mapper.canonicalize(n)[0]} = {self.mapper.canonicalize(name)[0]}\n")

    def generate_struct(self, struct):
        output = ""
        # TODO add typedef mapping for all public names of this struct
        if len(struct.public_names) > 0:
            name = struct.public_names[0]
        else:
            name = struct.private_name

        members = ""
        member_cnt = 1
        for member in struct.members:
            type_name = member.type
            if isinstance(member.type, (MidlUnionDef, MidlStructDef)):
                # handle nested unions/structs
                self.handle_typedef(member.type)
                if len(member.type.public_names) > 0:
                    type_name = member.type.public_names[0]
                else:
                    type_name = member.type.private_name

            if isinstance(type_name, str):
                members += (
                    f'({self.mapper.canonicalize(type_name)[0]}, "{member.name}"),'
                )
            member_cnt += 1

        class_def = f"""
class {self.mapper.canonicalize(name)[0]}(NdrStructure):
    MEMBERS = [{members}]

    
"""
        self.io.write(class_def)
        for n in struct.public_names:
            if n != name:
                n = n.replace("*","")
                #TODO still need to generate code to add this to the type alias lookup at runtime
                self.io.write(f"{self.mapper.canonicalize(n)[0]} = {self.mapper.canonicalize(name)[0]}\n")


    def generate_enum(self, enum):
        map =""
        for k in enum.map:
            map += f"({enum.map[k]} , '{k}'),"
        class_def = f"""
class {self.mapper.canonicalize(enum.public_names[0])[0]}(NdrEnum):
    MAP = ({map})        
"""
        self.io.write(class_def)

    def generate_interface(self, midl_interface):
        if len(midl_interface.attributes) == 0:
            return ""
        uuid = midl_interface.attributes["uuid"].params[0]
        if "version" in midl_interface.attributes:
            version = midl_interface.attributes["version"].params[0]
        else:
            version = "1.0"
        procedures = ""
        for typedef in midl_interface.typedefs:
            self.handle_typedef(typedef)
        self.io.write(f'Interface("{uuid}", "{version}",[')
        for proc in midl_interface.procedures:
            procedures += f"{self.generate_procedure(proc)},\n"
        self.io.write("])")

    def generate_procedure(self, procedure):
        output = ""
        params = ""
        for param in procedure.params:
            input_attr = "in" in param.attributes
            output_attr = "out" in param.attributes
            clz = (
                "InOut"
                if input_attr and output_attr
                else ("Out" if output_attr else ("In" if input_attr else None))
            )
            if clz is not None:
                params += f"{clz}(({self.mapper.canonicalize(param.type)[0]},'{param.name}')),\n"
        output += f'Method("{procedure.name}",\n{params}),'
        self.io.write(output)
