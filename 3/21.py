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

pattern = re.compile(r'^\[\[Category:.+\]\]$',re.MULTILINE + re.DOTALL)
contents = pattern.findall(UK())
for content in contents:
    print(content)