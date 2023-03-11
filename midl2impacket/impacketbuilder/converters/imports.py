import pathlib
import typing

from midl2impacket.midlparser import parse_idl
from midl2impacket.midltypes import MidlImport

from .base import Converter
from .comments import MidlCommentWriter


class MidlImportsConverter(Converter):
    def convert(self, imports: typing.List[MidlImport], import_dir: str, def_converter):
        comment_writer = MidlCommentWriter(self.io, self.tab_level)
        for _import in imports:
            comment_writer = MidlCommentWriter(self.io, self.tab_level)
            comment_writer.banner_comment(_import.file)
            in_file = pathlib.Path(import_dir + _import.file)
            def_converter.convert(parse_idl(in_file), import_dir)
