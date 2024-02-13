from sys import stdin
from collections import deque
N = int(input())

dots = deque()
for i in range(N):
    a, b = map(int, stdin.readline().split())
    dots.append((a,b))

dots = sorted(dots, key=lambda x: (x[0], x[1]))

for i in dots:
    print(i[0], i[1])