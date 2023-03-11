from re import L, M

from midl2impacket.midltypes import MidlDefinition

from .converters.definition import MidlDefinitionConverter
from .converters.static import MidlStaticConverter
from .converters.typing import IDL_TO_NDR, TypeMapper
from .ndrbuilder.io import PythonWriter


class ImpacketBuilder:
    """Converts a MIDL Definition into a Python module"""

    def __init__(self):
        self.__midl_def = None

    def midl_def(self, definition: MidlDefinition):
        self.__midl_def = definition
        return self

    def import_dir(self, dir: str):
        self.__import_dir = dir
        return self

    def build(self):
        assert self.__midl_def != None
        python_writer = PythonWriter()
        type_mapper = TypeMapper(python_writer)
        tabs = 0
        static_converter = MidlStaticConverter(python_writer, tabs, mapper=type_mapper)
        static_converter.convert()

        python_code = MidlDefinitionConverter(
            python_writer, tabs, mapper=type_mapper
        ).convert(self.__midl_def, self.__import_dir)
        return python_code
