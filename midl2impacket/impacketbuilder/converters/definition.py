from midl2impacket.midltypes import MidlDefinition

from .base import Converter
from .comments import MidlCommentWriter
from .constants import MidlConstantConverter
from .imports import MidlImportsConverter
from .interface import MidlInterfaceConverter


class MidlDefinitionConverter(Converter):
    def convert(self, definition: MidlDefinition, import_dir: str) -> str:
        # Instantiate all of the converters
        const_converter = MidlConstantConverter(
            self.io, tab_level=self.tab_level, mapper=self.mapper
        )
        interface_converter = MidlInterfaceConverter(
            self.io, tab_level=self.tab_level, mapper=self.mapper
        )
        imports_converter = MidlImportsConverter(
            self.io, self.tab_level, mapper=self.mapper
        )
        comment_writer = MidlCommentWriter(self.io, self.tab_level)

        # Do all of the conversion and writing
        imports_converter.convert(definition.imports, import_dir, self)
        comment_writer.banner_comment("TYPEDEFS")
        for typedef in definition.typedefs:
            interface_converter.handle_typedef(typedef)
        if len(definition.instantiation) > 0:
            comment_writer.banner_comment("CONSTANTS")
        for const in definition.instantiation:
            const_converter.convert(const)
        if len(definition.interfaces) > 0:
            comment_writer.banner_comment("INTERFACE DEFINITION")
        for interface in definition.interfaces:
            comment_writer.banner_comment(f"{interface.name} Definition")
            interface_converter.convert(interface, import_dir, self)
        return self.io.getvalue()
