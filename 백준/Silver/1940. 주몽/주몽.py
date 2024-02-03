from sys import stdin
N = int(input())
M = int(input())
l = list(sorted(map(int, stdin.readline().split())))

s, e, answer, sum = 0, N - 1, 0, 0
while s < e:
    sum = l[s] + l[e]
    if sum == M:
        s += 1
        e -= 1
        answer += 1
    elif sum < M :
        s += 1
    elif sum > M:
        e -= 1
print(answer)