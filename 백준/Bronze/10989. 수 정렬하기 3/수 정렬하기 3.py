from sys import stdin
import gc

N = int(stdin.readline())
l = [0] * 100001

for _ in range(N):
    l[int(stdin.readline())] += 1

del N
gc.collect()

for i, n in enumerate(l):
    if n != 0:
        for _ in range(n):
            print(i)
            
