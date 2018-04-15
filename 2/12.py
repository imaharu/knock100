import sys
col1 = open('col1.txt','w')
col2 = open('col2.txt','w')
col1_string = ""
col2_string = ""
with open('hightemp.txt') as f:
    for line in f:
        line = line.split('\t')
        col1_string += (line[0] + "\n")
        col2_string += (line[1] + "\n")
col1.write(col1_string)
col2.write(col2_string)