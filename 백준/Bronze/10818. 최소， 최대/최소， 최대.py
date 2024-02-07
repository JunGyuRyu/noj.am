from sys import stdin
from collections import deque
N = int(input())
l = deque(sorted(map(int, stdin.readline().split())))
min, max = 0, 0
if N == 1:
    min = max = l[0]
else:
    min = l.popleft()
    max = l.pop()
print(min, max)