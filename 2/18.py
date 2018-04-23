with open('hightemp.txt') as f:
    lines = f.readlines()
    lines = sorted(lines, key=lambda x:x.split()[2])

for line in lines:
    print(line,end="")