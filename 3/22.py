
        #m = re.search(r'Category:(?P<category>.+?)((\])|(\|))',line)


import json
import re
fname = 'jawiki-country.json'
def UK():

    with open(fname, 'r') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

    raise ValueError('イギリスの記事が見つからない')

pattern = re.compile(r'^\[\[Category:(?P<category>.+?)\]\]$',re.MULTILINE + re.DOTALL)
contents = pattern.findall(UK())

for content in contents:
    content = re.sub(r"\|\*","",content)
    pattern2 = re.compile(r'\|',re.MULTILINE + re.DOTALL)
    for content in pattern2.split(content):
        print(content)