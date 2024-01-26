from sys import stdin
N = int(input())
l = list(map(int, stdin.readline().split(" ")))
answer = 0
flag = True
for i in l:
    for j in range(2, i):
        if i % j == 0:
            flag = False
    if flag == True and i != 1:
        answer += 1
    flag = True
print(answer)