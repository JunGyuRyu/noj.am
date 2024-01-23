s = str(input())
tmp = ''
for i in s:
    if i == i.upper():
        tmp += i.lower()
    else:
        tmp += i.upper()
print(tmp)