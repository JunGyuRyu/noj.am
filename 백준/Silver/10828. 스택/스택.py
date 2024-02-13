from sys import stdin

N = int(input())
queue = []
for i in range(N):
    s = stdin.readline().strip()

    if s[:4] == 'push':
        a, b = s.split()
        queue.append(int(b))
    elif s == 'pop' or  s == 'top':
        if len(queue) == 0:
            print(-1)
        else:
            tmp = queue.pop()
            print(tmp)
            if s == 'top':
                queue.append(tmp)
    elif s == 'size':
        print(len(queue))
    elif s == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)