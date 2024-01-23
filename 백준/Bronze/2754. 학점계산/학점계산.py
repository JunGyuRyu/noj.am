s = str(input())
try:
    a, b, num = s[0], s[1], 0.0
    if b == "+":
        num += 0.3
    elif b == "-":
        num -= 0.3

    if a == "A":
        num += 4.0
    elif a == "B":
        num += 3.0
    elif a == "C":
        num += 2.0
    elif a == "D":
        num += 1.0
except:
    num = 0.0
print(num)