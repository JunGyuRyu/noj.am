H, M = map(int, input().split())
m = M - 45
if m < 0:
    H -= 1
    m = 60 + m
    if H < 0:
        H = 24 + H
print(H, m)