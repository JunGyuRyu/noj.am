def solution(n):
    answer = []
    now = [0,n-1]
    go = ['d', 'l', 'u', 'r']
    flag = 0
    val = n + 1
    for i in range(n):
        answer.append([])
        for j in range(n):
            answer[i].append(0)

    for i in range(1, n+1):
        answer[0][i-1] = i
    
    for i in range(n-1, 0, -1):
        for j in range(2):
            for k in range(1, i+1):
                # 여기에서 행렬에 값 넣으면 끝
                if go[flag] == 'r':
                    now = [now[0], now[1]+1]
                    answer[now[0]][now[1]] = val
                    val += 1
                if go[flag] == 'd':
                    now = [now[0]+1, now[1]]
                    answer[now[0]][now[1]] = val
                    val += 1
                if go[flag] == 'l':
                    now = [now[0], now[1]-1]
                    answer[now[0]][now[1]] = val
                    val += 1
                if go[flag] == 'u':
                    now = [now[0]-1, now[1]]
                    answer[now[0]][now[1]] = val
                    val += 1
            if flag == 3:
                flag = 0
            else:
                flag += 1 
    return answer