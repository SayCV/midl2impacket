import argparse
import pathlib
import re


class MidlPreprocessorException(Exception):
    pass

def get_encoding(filename):
    import chardet
    with open(filename, "rb") as f:
        res = chardet.detect(f.read())
    return res['encoding']

def add_idl_comment(match_obj):
    prefix = '//'
    ret = ''
    if match_obj.group(1) is not None:
        ret = prefix + match_obj.group(1)
    return ret

def preprocess_directory(
    input_dir: pathlib.Path,
    output_dir: pathlib.Path
):
    for idl_file in input_dir.glob("*.idl"):
        pp_cmd = f"fix {idl_file.as_posix()}"
        print(pp_cmd)
        output_file = output_dir / idl_file.name

        data: str = idl_file.read_text(encoding=get_encoding(idl_file), errors='ignore')
        if not data:
            raise MidlPreprocessorException(f"File `{idl_file}` is empty")
        
        global mc1
        global mc2
        mc1 = 0
        mc2 = 0
        mc3 = 0
        lines = []
        for line in data.split('\n'):
            pattern = u'(^\s*importlib\("[.\w]+"\);\s?)'
            p_obj = re.compile(pattern)
            if p_obj.search(line):
                mc1 += 1 # len( re.compile(pattern).findall(line) )
                line = re.sub(p_obj, add_idl_comment, line)

            pattern = u'(^\s*[disp]{,4}interface\s\w+;\s?)'
            p_obj = re.compile(pattern)
            if p_obj.search(line):
                mc2 += 1 # len( re.compile(pattern).findall(line) )
                line = re.sub(p_obj, add_idl_comment, line)

            pattern = u'(\)public\])'
            p_obj = re.compile(pattern)
            if p_obj.search(line):
                mc3 += 1 # len( re.compile(pattern).findall(line) )
                line = re.sub(p_obj, u')]', line)

            lines.append(line)

        print(f'Matched found total : {mc1 + mc2 + mc3}, pattern 1 found {mc1}, pattern 2 found {mc2}, pattern 3 found {mc3}')

        output_file.write_text('\n'.join(lines), encoding='utf-8', errors='ignore')
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
