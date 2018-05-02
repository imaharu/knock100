# cut -f 1 hightemp.txt | sort | uniq -c | sort
import sys
col_string = []
with open('hightemp.txt') as f:
    for line in f:
        line = line.split('\t')
        col_string.append(line[0])

print(col_string)