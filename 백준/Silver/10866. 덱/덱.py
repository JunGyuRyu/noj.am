from sys import stdin, stdout
from collections import deque

l = ['push_front', 'push_back', 'pop_front', 'pop_back', 'size', 'empty', 'front', 'back']
N = int(stdin.readline())
dq = deque()
for _ in range(N):
    sen = stdin.readline().strip()
    if l[0] in sen:
        dq.appendleft(int(sen[11:]))
    elif l[1] in sen:
        dq.append(int(sen[10:]))
    elif sen == l[2]:
        stdout.write(str(dq.popleft()) + '\n' if len(dq) != 0 else '-1'  + '\n')
    elif sen == l[3]:
        stdout.write(str(dq.pop()) + '\n' if len(dq) != 0 else '-1'  + '\n')
    elif sen == l[4]:
        stdout.write(str(len(dq)) + '\n')
    elif sen == l[5]:
        stdout.write('1' + '\n' if len(dq) == 0 else '0' + '\n')
    elif sen == l[6]:
        stdout.write(str(dq[0]) + '\n' if len(dq) != 0 else '-1' + '\n')
    elif sen == l[7]:
        stdout.write(str(dq[-1]) + '\n' if len(dq) != 0 else '-1' + '\n')