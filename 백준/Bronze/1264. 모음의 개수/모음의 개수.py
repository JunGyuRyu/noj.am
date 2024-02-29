from sys import stdin, stdout

while True:
    s = stdin.readline().strip()
    if s == "#":
        break
    print(s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("A") + s.count("E") + s.count("I") + s.count("O") + s.count("u") + s.count("U"))