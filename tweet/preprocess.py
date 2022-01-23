import re

# 分析にかけやすいように前処理を行います。
def preprocess(list_yet):
    list_processed = []

    ptnRT = re.compile(r'RT')
    ptnReply = re.compile(r"@([A-Za-z0-9_]+)")
    ptnURL = re.compile(r'(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)')
    ptnHash = re.compile(r'#(\w+)')
    
    for sentence in list_yet:
        sub = re.sub(ptnHash,"",sentence)
        if (re.search(ptnRT,sentence) or re.search(ptnReply,sentence) or re.search(ptnURL,sentence)) == None:
            list_processed.append(sub)
            
    return list_processed