from sys import stdin

N, M = map(int, stdin.readline().split())
l = list(sorted(map(int, stdin.readline().split())))
idx_len = len(l)
max = 0
p1, p2, p3 = -1, -2, -3
while True:
    if abs(p1) == idx_len - 2:
        break
    tmp = l[p1] + l[p2] + l[p3]
    if tmp <= M:
        if tmp >= max:
            max = tmp
    if abs(p3) != idx_len:
        p3 -= 1
    elif abs(p3) == idx_len and abs(p2) != idx_len - 1:
        p2 -= 1
        p3 = p2-1
    elif abs(p3) == idx_len and abs(p2) == idx_len - 1 and abs(p1) != idx_len - 2:
        p1 -= 1
        p2 = p1 - 1
        p3 = p1 - 2
print(max)