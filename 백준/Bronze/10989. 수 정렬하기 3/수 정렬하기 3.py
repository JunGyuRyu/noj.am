from sys import stdin

N = int(stdin.readline())
l = [0] * 100001

for _ in range(N):
    tmp = int(stdin.readline())
    l[tmp] += 1

for i, n in enumerate(l):
    if n != 0:
        for _ in range(n):
            print(i)