import random
def typoglycemia(words):
    for word in words:
        if len(word) < 4 :
            pass
        else:
            word = list(word)
            center_list = word[1:-1]
            random.shuffle(center_list)
            word = word[0] + "".join(center_list) + word[-1]
        shuffled.append(word)

string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = string.split(" ")
shuffled = []
typoglycemia(words)
print(shuffled)