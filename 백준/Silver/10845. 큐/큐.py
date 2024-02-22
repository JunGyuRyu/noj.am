from sys import stdin, stdout
from collections import deque
N = int(input())
l = ['push', 'pop', 'size', 'empty', 'front', 'back']
dq = deque()
for _ in range(N):
    s = stdin.readline().strip()
    if l[0] in s:
        s, n = s.split()
        dq.append(int(n))
    elif s == l[1]:
        print(-1 if len(dq) == 0 else dq.popleft())
    elif s == l[2]:
        print(len(dq))
    elif s == l[3]:
        print(1 if len(dq) == 0 else 0)
    elif s == l[4]:
        print(-1 if len(dq) == 0 else dq[0])
    elif s == l[5]:
        print(-1 if len(dq) == 0 else dq[-1])