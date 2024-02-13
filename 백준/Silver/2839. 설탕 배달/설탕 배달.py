from sys import stdin
N = int(input())

def dp(n, answer, five):
    if n <= N:
        if n % 3 == 0:
            answer += int(n / 3)
            print(answer)
        elif n <= N:
            n += 5
            answer -= 1
            dp(n, answer, five)
    else:
        print(-1)


if N % 5 == 0:
    print(int(N / 5))
elif N > 3:
    n = N % 5
    answer = int(N / 5)
    dp(n, answer, 0)
elif N % 3 == 0:
    print(int(N / 3))
else:
    print(-1, "예외")