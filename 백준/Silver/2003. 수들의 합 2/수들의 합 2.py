from sys import stdin
N, M = map(int, stdin.readline().split())
l = list(map(int, stdin.readline().split()))

s, e, answer, sum = 0, 0, 0, 0
while True:
    if sum >= M:
        sum -= l[s]
        s += 1
    elif e == N:
        break
    else:
        sum += l[e]
        e += 1
    if sum == M:
        answer += 1
print(answer)