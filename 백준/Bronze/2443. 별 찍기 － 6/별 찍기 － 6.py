from sys import stdin, stdout
n = int(stdin.readline())
for i in range(n):
    stdout.write(" " * i + "*" * (((n - i - 1) * 2) + 1) + '\n')