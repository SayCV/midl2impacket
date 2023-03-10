import re
import argparse
import pathlib

class MidlPreprocessorException(Exception):
    pass

global matched1_count
global matched2_count
def add_idl_comment(match_obj):
    global matched1_count
    global matched2_count
    prefix = '//'
    ret = ''
    if match_obj.group(1) is not None:
        matched1_count += 1
        ret = prefix + match_obj.group(1)
    if match_obj.group(2) is not None:
        matched2_count += 1
        ret = prefix + match_obj.group(2)
    return ret

def preprocess_directory(
    input_dir: pathlib.Path,
    output_dir: pathlib.Path
):
    for idl_file in input_dir.glob("*.idl"):
        pp_cmd = f"fix {idl_file.as_posix()}"
        print(pp_cmd)
        output_file = output_dir / idl_file.name

        data: str = idl_file.read_text(encoding='utf-8', errors='ignore')
        if not data:
            raise MidlPreprocessorException(f"File `{idl_file}` is empty")

        pattern = r'^(\S*importlib\(".*.tlb"\);\s*) | (^\S*[a-zA-Z]{,4}interface \w*;\s*)'
        global matched1_count
        global matched2_count
        matched1_count = 0
        matched2_count = 0
        data = re.sub(pattern, add_idl_comment, data)
        print(f'Matched found total : {matched1_count + matched2_count}, pattern 1 found {matched1_count}, pattern 2 found {matched2_count}')

        output_file.write_text(data, encoding='utf-8', errors='ignore')
        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--in-dir", help='Input IDL directory e.g. "scraped"', required=True
    )
    parser.add_argument(
        "--out-dir",
        help='Output directory e.g. "preprocessed". NOTE: If the preprocessor already writes to a file, \
              this directory will contain stdout for each invocation',
        required=False
    )

    args = parser.parse_args()
    input_dir = pathlib.Path(args.in_dir)
    if not input_dir.exists() or not input_dir.is_dir():
        raise MidlPreprocessorException(
            f"Provided input directory {args.in_dir} doesn't exist or isn't a directory!"
        )

    if args.out_dir is None:
        output_dir = pathlib.Path(args.in_dir)
    else:
        output_dir = pathlib.Path(args.out_dir)
    #output_dir.mkdir(exist_ok=True)

    preprocess_directory(input_dir, output_dir)


if __name__ == "__main__":
    main()
