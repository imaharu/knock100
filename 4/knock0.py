def create_data():
    with open("neko.txt.mecab") as f:
        morphemes = []
        for line in f:
            cols = line.split('\t')
            if(len(cols) < 2):
                raise StopIteration 
            res_cols = cols[1].split(',')
            morpheme = {
                'surface': cols[0],
                'base': res_cols[6],
                'pos': res_cols[0],
                'pos1': res_cols[1]
            }
            morphemes.append(morpheme)
            if res_cols[1] == "句点":
                yield morphemes
                morphemes = []