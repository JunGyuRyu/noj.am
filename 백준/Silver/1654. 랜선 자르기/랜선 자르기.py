K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

max_val = max(arr) + 1
min_val = 0

while min_val < max_val:
    mid = (max_val + min_val) // 2
    count = sum([arr[i] // mid for i in range(len(arr))])
    if count < N:
        max_val = mid
    else:
        min_val = mid + 1
print(min_val - 1)