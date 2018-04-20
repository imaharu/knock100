import sys
col1_string = []
with open('hightemp.txt') as f:
    for line in f:
        line = line.split('\t')
        if line[0] not in col1_string:
            col1_string.append(line[0])
    #print(str(col1_string).decode('string-escape'))
    print(col1_string)