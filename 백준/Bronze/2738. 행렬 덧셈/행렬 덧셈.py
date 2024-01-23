from sys import stdin
N, M = map(int, stdin.readline().split(" "))
answer = []
for i in range(N):
    answer.append([_ for _ in map(int, stdin.readline().split(" "))])
for j in range(N):
    for i, n in enumerate(map(int, stdin.readline().split(" "))):
        answer[j][i] += n
for s in answer:
    print(" ".join(map(str, s)))