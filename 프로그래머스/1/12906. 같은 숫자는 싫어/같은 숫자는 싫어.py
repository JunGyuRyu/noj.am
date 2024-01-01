def solution(arr):
    return [n for i, n in enumerate(arr) if arr[i-1:i:] != arr[i:i+1:]]