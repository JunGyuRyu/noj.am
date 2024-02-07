from sys import stdin
N = int(input())
l = list(map(int, stdin.readline().split()))
max = max(l)
for i in range(len(l)):
    l[i] *= 100 / max
print(sum(l)/N)