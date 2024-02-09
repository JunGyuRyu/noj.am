from sys import stdin
input = lambda: stdin.readline().rstrip()
N = input()

for i in range(int(N)):
    n, s = input().split()
    tmp = ''
    for j in s:
        for k in range(int(n)):
            tmp += j
    print(tmp)
    