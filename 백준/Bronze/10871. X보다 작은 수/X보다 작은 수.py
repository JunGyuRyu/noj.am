from sys import stdin
N, X = map(int, stdin.readline().split(" "))
A = " ".join([x for x in stdin.readline().split(" ") if int(x) < X ])
print(A)