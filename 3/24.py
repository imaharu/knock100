import re
with open('article.txt') as f:
    for line in f:
        m = re.search(r'ファイル:(?P<filename>.+?)(\|)',line)
        if m:
            print(m.group("filename"))