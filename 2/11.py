import sys
with open('hightemp.txt') as f:
    for line in f:
        line = line.replace('\t',' ')
        sys.stdout.write(line)