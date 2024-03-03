tot = 0
for _ in range(4):
    tot += int(input().strip())
print(tot // 60)
print(tot % 60)