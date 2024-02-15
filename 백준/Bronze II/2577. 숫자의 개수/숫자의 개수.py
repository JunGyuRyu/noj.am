from sys import stdin, stdout
tot = 1
l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for _ in range(3):
    tot *= int(stdin.readline().strip())

for i in str(tot):
    l[int(i)] += 1
    
for n in l:
    stdout.write(str(n)+'\n')