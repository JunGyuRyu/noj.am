def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    
    # 중복 제거
    for i in range(1, n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
    
    answer = n
    check_list = []
    
    for n in reserve:
        if n-1 in lost and n not in check_list:
            check_list.append(n-1)
            lost.remove(n-1)
        elif n+1 in lost and n not in check_list:
            check_list.append(n+1)
            lost.remove(n+1)
    print(lost, reserve)
    return answer - len(lost)