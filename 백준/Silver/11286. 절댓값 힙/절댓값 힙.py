from queue import PriorityQueue

import sys

input = lambda : sys.stdin.readline().rstrip()
print = lambda x : sys.stdout.write(str(x) + '\n')

N = int(input())
pqueue = PriorityQueue()

for i in range(N):
    n = int(input())

    if n == 0:
        if pqueue.empty():
            print(0)
        else:
            print(pqueue.get()[1])
    else:
        pqueue.put((abs(n), n))