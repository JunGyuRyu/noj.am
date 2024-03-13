from sys import stdin, stdout

n = int(stdin.readline())
for i in range(n):
    stdout.write(" " * i)
    stdout.write(str("*" * ((n - i - 1) * 2 + 1) + '\n'))
for i in range(n-1):
    stdout.write(" " * (n - i - 2))
    stdout.write(str("*" * (i * 2 + 3) + '\n'))
