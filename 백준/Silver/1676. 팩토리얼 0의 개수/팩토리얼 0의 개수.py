import math
N = int(input())
num = math.factorial(N)
answer = 0
for i in str(num)[::-1]:
    if int(i) != 0:
        print(answer)
        exit()
    answer += 1