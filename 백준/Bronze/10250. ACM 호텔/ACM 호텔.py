from sys import stdin, stdout
input = stdin.readline
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    y = N % H
    x = int(N / H) + 1
    if y == 0:
        y = H
        x -= 1
    y = str(y)
    if x < 10:
        x = '0' + str(x)
    else:
        x = str(x)
    stdout.write(str(int(y + x)) + '\n')