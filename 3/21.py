import re
with open('article.txt') as f:
    for line in f:
        if re.search(r'Category:',line):
            print(line,end="")

print("\n")