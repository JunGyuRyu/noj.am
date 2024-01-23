from sys import stdin
def thing(a, b):
    return (a+b) * (a-b)

a, b = map(int, stdin.readline().split(" "))
print(thing(a, b))