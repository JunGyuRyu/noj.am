from sys import stdin
from collections import deque
bs = int(input())
apple_loc = [list(map(int,stdin.readline().split())) for i in range(int(input()))]
rotate_snake = [list(stdin.readline().split()) for i in range(int(input()))]

tmp = [i for i in dict(rotate_snake).keys()]
for i, n in enumerate(tmp[1::]):
    rotate_snake[i+1][0] = str(int(n) - int(tmp[i]))

if rotate_snake[0][1] == 'L':
    print({rotate_snake[0][0]})
    exit()

def make_board(bs, apple_loc):
    board = [[0 for col in range(bs)] for row in range(bs)]

    for row, col in apple_loc:
        board[row-1][col-1] = 1
    return board

board = make_board(bs, apple_loc)
head_loc = [0, 0] # [row, col]
head_to_go = [head_loc[0], head_loc[1] + 1]
snake = deque([head_loc])
p_time = 1
trial = 0
direction = 'D'

def game_start(rotate_snake, head_loc, head_to_go, p_time, trial):
    for st, di in rotate_snake:
        direction = di
        head_di = [head_to_go[0] - head_loc[0], head_to_go[1] - head_loc[1]]
        if head_di[0] == 0:
            di_to_go = 0
        else:
            di_to_go = 1

        for i in range(int(st)):
            if head_loc != [0,0] or trial != 0:
                end_condition = (head_to_go in snake) or (head_to_go[0] >= bs or head_to_go[0] < 0) or (head_to_go[1] >= bs or head_to_go[1] < 0)
            else:
                end_condition = False

            if end_condition:
                print(p_time)
                exit()
            else:
                p_time += 1
                snake.append(head_to_go)
                if board[head_to_go[0]][head_to_go[1]] == 0:
                    snake.popleft()
                else:
                    board[head_to_go[0]][head_to_go[1]] = 0
                head_loc = head_to_go
                head_to_go = [head_to_go[0] + head_di[0], head_to_go[1] + head_di[1]]
        if di_to_go == 0:
            if head_di[1] == 1:
                check_DL = 1 if direction == 'D' else -1
                head_di = [abs(head_di[1]) * check_DL, abs(head_di[0])]
                head_to_go = [head_loc[0] + check_DL, head_loc[1]]
            else:
                check_DL = -1 if direction == 'D' else 1
                head_di = [abs(head_di[1]) * check_DL, abs(head_di[0])]
                head_to_go = [head_loc[0] + check_DL, head_loc[1]]
        else:
            if head_di[0] == 1:
                check_DL = -1 if direction == 'D' else 1
                head_di = [abs(head_di[1]), abs(head_di[0]) * check_DL]
                head_to_go = [head_loc[0], head_loc[1] + check_DL]
            else:
                check_DL = 1 if direction == 'D' else -1
                head_di = [abs(head_di[1]), abs(head_di[0]) * check_DL]
                head_to_go = [head_loc[0], head_loc[1] + check_DL]
    trial += 1
    if end_condition == False:
        game_start(rotate_snake, head_loc, head_to_go, p_time, trial)
        
game_start(rotate_snake, head_loc, head_to_go, p_time, trial)
