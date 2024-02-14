from sys import stdin

N = int(input())
streak, answer = 0, 0
for i in range(N):
    s = stdin.readline().strip()
    for i in s:
        if i == 'O':
            streak += 1
            answer += streak
        else:
            streak = 0
    print(answer)
    streak, answer = 0, 0