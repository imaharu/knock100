import json
import re
articles={}

f = open('jawiki-country.json', 'r')
i = 0

for line in f:
    articles[i]=json.loads(line)
    i+=1
f.close()

for key, value in articles.items():
    if re.match(u'イギリス', articles[key]["title"]):
        print(articles[key]["text"])