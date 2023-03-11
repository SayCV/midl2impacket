
def get_encoding(filename):
    import chardet
    with open(filename, "rb") as f:
        res = chardet.detect(f.read())
    return res['encoding']
