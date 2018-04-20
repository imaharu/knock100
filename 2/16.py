import sys 
argvs = sys.argv
N = int(argvs[1])
count = 0
with open('hightemp.txt') as f:
    for line in f:
        if count % N == 0:
            print(line.replace("\n","") + "\n")
        else:
            print(line.replace("\n",""))
        count += 1