from sys import stdin
while True:
    try:
        a, b = map(int, stdin.readline().split(" "))
        print(a + b)    
    except:
        break