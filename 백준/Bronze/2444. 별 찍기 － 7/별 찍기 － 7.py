from sys import stdin, stdout
n = int(stdin.readline())
for i in range(n):
    stdout.write(" " * (n - i - 1) + "*" * ((i * 2) + 1) + '\n')
for i in range(n):
    stdout.write(" " * (i + 1) + "*" * (((n - i - 2) * 2) + 1) + '\n')