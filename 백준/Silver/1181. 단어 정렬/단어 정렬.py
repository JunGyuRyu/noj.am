from sys import stdin
answer = [stdin.readline().strip() for i in range(int(input()))]
answer = sorted(list(set(answer)))
answer = sorted(answer, key=lambda x: len(x))
for i in answer:
    print(i)