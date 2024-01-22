def solution(n, lost, reserve):
    answer = n
    lost = sorted(lost)
    reserve = sorted(reserve)
    # check_list = []
    
    # 중복 제거
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