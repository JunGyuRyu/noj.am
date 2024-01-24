def solution(n, lost, reserve):
    answer = n
    lost, reserve = sorted(lost), sorted(reserve)
    
    for i in range(1, n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
    for n in reserve:
        if n-1 in lost:
            lost.remove(n-1)
        elif n+1 in lost:
            lost.remove(n+1)
    return answer - len(lost)