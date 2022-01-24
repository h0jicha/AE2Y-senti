import re


def preprocess(path_input, path_output):
    list_processed = []

    ptnRT = re.compile(r'RT')
    ptnReply = re.compile(r"@([A-Za-z0-9_]+)")
    ptnURL = re.compile(
        r'(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)')
    ptnHash = re.compile(r'#(\w+)')

    with open(path_input, encoding="utf-8") as f:
        for line in f:
            sub = re.sub(ptnHash, "", line)
            if (re.search(ptnRT, line) or re.search(ptnReply, line) or re.search(ptnURL, line)) == None:
                list_processed.append(sub)

    fname = r"'" + path_output + "'"
    fname = fname.replace("'", "")

    with open(fname, "w", encoding="utf-8") as f:
        f.writelines(list_processed)
