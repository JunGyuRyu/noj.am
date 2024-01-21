from sys import stdin
input = lambda: stdin.readline().rstrip()
n = int(input())
for i in range(n):
    a, b = map(int, input().split(" "))
    print(a + b)