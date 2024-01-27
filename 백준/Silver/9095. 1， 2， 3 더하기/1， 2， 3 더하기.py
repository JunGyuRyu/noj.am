from sys import stdin
T = int(input())
a, b, c = 1, 2, 4
l = [a, b, c]

for i in range(11):
    l.append(l[-1]+l[-2]+l[-3])

for i in range(T):
    n = int(input())
    print(l[n -1])