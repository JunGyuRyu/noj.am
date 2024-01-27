T = int(input())
l = [1, 2, 4]
for i in range(11):
    l.append(l[-1]+l[-2]+l[-3])
for i in range(T):
    print(l[int(input()) -1])