import re
with open('article.txt') as f:
    for line in f:
        m = re.search(r'==(?P<section>.+?)==',line)
        if m:
            print(re.sub(r'(=)', "", m.group("section")),len(re.findall('=+', m.group("section"))) + 1)