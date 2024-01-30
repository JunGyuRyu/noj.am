from sys import stdin
N = int(stdin.readline())
l = [ int(stdin.readline()) for _ in range(N)]
for n in sorted(l):
    print(n)