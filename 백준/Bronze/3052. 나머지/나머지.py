from sys import stdin
l = [int(input()) for i in range(10)]
l2 = [i % 42 for i in l]

print(len(set(l2)))