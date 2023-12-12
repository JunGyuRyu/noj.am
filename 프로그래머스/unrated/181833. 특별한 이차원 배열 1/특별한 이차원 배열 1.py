def solution(n):
    answer = []
    for i in range(n):
        answer.insert(i, [0 for j in range(n)])
        answer[i][i] = 1
    return answer