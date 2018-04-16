import sys 
argvs = sys.argv

N = int(argvs[1])
count = 0
with open('hightemp.txt') as f:
    for line in f:
        print(line, end='')
        count += 1
        if count == N :
            break