from knock0 import create_data

lines = create_data() 
all_verb = set()
for line in lines:
    for morpheme in line:
        if morpheme['pos'] == '動詞':
            all_verb.add(morpheme['surface'])
print(all_verb)