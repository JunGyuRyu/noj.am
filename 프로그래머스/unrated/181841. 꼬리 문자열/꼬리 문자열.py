def solution(str_list, ex):
    answer = ''
    for i, s in enumerate(str_list):
        if ex not in str_list[i]:
            answer += s
    return answer