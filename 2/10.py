# wc -l hightemp.txt
file = open('hightemp.txt')
count = 0
with file as f:
    for line in f:
        count += 1

print(count)