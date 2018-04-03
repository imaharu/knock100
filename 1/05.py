def n_gram(size,string):
    # result = [string[i: i+size] for i in range(0, len(string), size)]
    mogi = []
    for i in range(0,len(string) - 1):
        mogi.append(string[i:i+size:1])
    return mogi




string = "I am an NLPer"
word = string.split(" ")

# 単語bi-gram
bi_gram = n_gram(2,word)
print(bi_gram)


# 文字bi-gram
bi_gram = n_gram(2,string)
print(bi_gram)