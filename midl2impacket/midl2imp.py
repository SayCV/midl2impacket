import argparse
import logging
import pathlib

from midl2impacket import midltypes
from midl2impacket.fuzzer.template_generator import FuzzerTemplateGenerator
from midl2impacket.impacketbuilder import ImpacketBuilder
from midl2impacket.midlparser import parse_idl

logging.basicConfig(style="{", format="[{levelname:<7}] {message}", level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def generate_impacket(midl_def: midltypes.MidlDefinition, import_dir: str):
    return ImpacketBuilder().midl_def(midl_def).import_dir(import_dir).build()


def generate_template(midl_def: midltypes.MidlDefinition, import_dir: str):
    return FuzzerTemplateGenerator().generate(midl_def, import_dir)


def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "--in-file",
        "-in",
        type=str,
        help="IDL file to convert to Impacket",
        required=True,
    )
    parser.add_argument(
        "--out-file",
        "-out",
        type=str,
        help="Impacket output file",
        default=None,
        required=False,
    )
    parser.add_argument(
        "--import-dir",
        "-imp",
        type=str,
        help="IDL imports directory",
        default="./",
        required=False,
    )

    args = parser.parse_args()
    generate(in_file=args.in_file, out_file=args.out_file, import_dir=args.import_dir)


def generate(in_file, out_file, import_dir):
    logger.info(f"Parsing {in_file}")
    in_file = pathlib.Path(in_file)
    if not in_file.exists():
        raise Exception(f"Provided input file {in_file} does not exist.")

    if not out_file:
        out_file = (in_file.parent / (in_file.stem + '_impacket')).with_suffix(".py")
    out_file = pathlib.Path(out_file)
    out_file.parent.mkdir(exist_ok=True)

    midl_def = parse_idl(in_file)
    if hasattr(midl_def, 'typedefs'):
        simple_typedefs = []
        for typedef in midl_def.typedefs:
            if isinstance(typedef, midltypes.MidlSimpleTypedef):
                simple_typedef = {}
                simple_typedef["name"] = typedef.name
                simple_typedef["type"] = typedef.type
                simple_typedefs.append(simple_typedef)

            elif isinstance(typedef, midltypes.MidlEnumDef):
                for simple_typedef in simple_typedefs:
                    if simple_typedef["type"] in typedef.public_names:
                        typedef.public_names.remove(simple_typedef["type"])
                        typedef.public_names.append(simple_typedef["name"])

        for idx, typedef in enumerate(midl_def.typedefs):
            if isinstance(typedef, midltypes.MidlSimpleTypedef):
                midl_def.typedefs.pop(idx)

    generated_code = generate_impacket(midl_def, import_dir)
    generated_template, uuid = generate_template(midl_def, import_dir)
    template_out = pathlib.Path(f"generated_fuzzers/{uuid}.py")
    template_out.parent.mkdir(exist_ok=True)

    template_out.write_text(generated_template, encoding='utf-8')
    logger.info(f'{template_out} done.')
    out_file.write_text(generated_code, encoding='utf-8')
    logger.info(f'{out_file} done.')


if __name__ == "__main__":
    main()
