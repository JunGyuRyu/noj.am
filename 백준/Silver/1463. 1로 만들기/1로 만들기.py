N = int(input())
def function(x):
    if x <= 3:
        return 1 if x != 1 else 0
    return min(function(x // 3) + x % 3 + 1, function(x // 2) + x % 2 + 1)
print(function(N))