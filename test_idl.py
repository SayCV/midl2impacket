
from midl2impacket import generate

def main():
    in_file1 = 'preprocessed/ms-wkst.idl'
    out_file1 = 'generated/ms-wkst.py'

    in_file2 = 'unprocessed/demo1.fix.IDL'
    out_file2 = 'generated/demo1.py'

    import_dir = "preprocessed/"

    if "x2" == "x1":
        generate(in_file=in_file1, out_file=out_file1, import_dir=import_dir)
    else:
        generate(in_file=in_file2, out_file=out_file2, import_dir=import_dir)

if __name__ == "__main__":
    main()