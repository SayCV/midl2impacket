import pathlib

from midl2impacket.midlparser.parsers.base import MidlParserException
from midl2impacket.midlparser.parsers.midl import MidlParser
from midl2impacket.midlparser.tokenizer import MidlTokenizer
from midl2impacket.util import get_encoding


def parse_idl(idl_file: pathlib.Path):
    data = idl_file.read_text(encoding=get_encoding(idl_file), errors='ignore')
    if not data:
        raise MidlParserException(f"File `{idl_file}` is empty")
    tokenizer = MidlTokenizer(data, idl_file.name)
    tokens = tokenizer.get_token()
    first_token = next(tokens)
    return MidlParser(tokens, tokenizer).parse(first_token)
