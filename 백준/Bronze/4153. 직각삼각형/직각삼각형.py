from sys import stdin

while True:
    l = sorted(list(map(int, stdin.readline().split())))
    if l.count(0) == 3 :
        break
    elif l[0]**2 + l[1]**2 == l[2]**2:
        print("right")
    else:
        print("wrong")