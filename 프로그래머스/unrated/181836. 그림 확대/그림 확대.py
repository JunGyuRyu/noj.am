def solution(picture, k):
    answer = ['']*len(picture)*k
    for i, st in enumerate(picture):
        for s in st:
            for j in range(k):
                answer[i*k+j] += s*k
    return answer