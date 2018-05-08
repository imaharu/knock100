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

dics = {}
pattern = re.compile(r'^\{\{基礎情報.+?^\}\}',re.MULTILINE + re.DOTALL)
basic_infos = pattern.findall(UK())
   
pattern = re.compile(r'^\|(?P<key>.+?).=.(?P<vaule>.+?)\n',re.MULTILINE + re.DOTALL)
contents = pattern.findall(basic_infos[0])


for content in contents:
    dics[content[0]] =  content[1]
