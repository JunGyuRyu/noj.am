def solution(order):
    answer = 4500 * len(order)
    for i in order:
        if 'latte' in i:
            answer += 500
    return answer