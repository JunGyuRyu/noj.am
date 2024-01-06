from sys import stdin
n = int(input())
result = 0
for i in range(3, n-5, 3):
    for j in range(3, n-2-i, 3):
        result += 1
print(result)