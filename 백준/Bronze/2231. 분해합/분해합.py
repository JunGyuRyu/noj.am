N = int(input())
flag = 0
for i in range(N):
    tmp = 0
    for j in str(i):
        tmp += int(j)
    tmp += i
    if tmp == N:
        print(i)
        flag = 1
        break
if flag == 0:
    print(0)