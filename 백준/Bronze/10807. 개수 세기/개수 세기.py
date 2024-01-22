from sys import stdin
N = int(input())
l = list(map(int, stdin.readline().split(" ")))
V = int(input())
print(l.count(V))