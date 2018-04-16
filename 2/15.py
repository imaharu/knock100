import sys 
argvs = sys.argv

N = int(argvs[1])
count = 0
with open('hightemp.txt') as f:
    get_line = len(f.readlines())
with open('hightemp.txt') as f:
    for line in f:
        count += 1
        if count > (get_line - N) :
            print(line, end='')