import re
flag = False
dic = {}
count = 1
before = ""
with open('article.txt') as f:
    for line in f:
        if flag:
            m = re.match(r'\|(?P<key>.+?) = (?P<value>.+)',line)
            if m:
                dic[m.group("key")] = m.group("value")
                before = m.group("key")
            else :
                dic[before] += line
        if re.search(r'{{基礎情報',line):
            flag = True
        elif re.match(r'}}',line):
            flag = False

print(dic)