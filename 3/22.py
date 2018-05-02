import re
with open('article.txt') as f:
    for line in f:
        m = re.search(r'Category:(?P<category>.+?)((\])|(\|))',line)
        if m:
            print(m.group("category"))