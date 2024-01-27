N = int(input())
l = sorted(list(map(int, input().split())))
t = 0
for i in range(N):
    t += sum(l[:i+1])
print(t)