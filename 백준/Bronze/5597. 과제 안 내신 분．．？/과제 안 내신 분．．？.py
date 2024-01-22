from sys import stdin
tmp_l = [i for i in range(1, 31)]
for i in range(28):
    n = int(input())
    tmp_l.remove(n)
for i in sorted(tmp_l):
    print(i)