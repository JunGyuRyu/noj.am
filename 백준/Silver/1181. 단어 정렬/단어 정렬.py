answer = [input() for i in range(int(input()))]
answer = sorted(list(set(answer)))
answer = sorted(answer, key=lambda x: len(x))
for i in answer:
    print(i)