import sys
file = open('diff.txt','w')
string = ""
with open('hightemp.txt') as f:
    for line in f:
        line = line.replace('\t',' ')
        # sys.stdout.write(line)
        string += line
file.write(string)