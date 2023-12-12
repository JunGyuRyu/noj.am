def solution(arr):
    answer = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                answer += 1
    return 1 if answer == len(arr)**2 else 0
    # return int(arr == list(map(list, zip(*arr))))