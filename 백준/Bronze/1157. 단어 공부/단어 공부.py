from sys import stdin

s = input().lower()
if len(s) == 1:
    print(s.upper())
    exit()

set_s = list(set(s))
if len(set_s) == 1:
    print(set_s[0].upper())
    exit()

set_s = sorted(set_s, key=lambda x: s.count(x))

first = set_s.pop()
second = set_s.pop()

count1 = s.count(first)
count2 = s.count(second)

if count1 == count2:
    print("?")
else:
    print(first.upper())