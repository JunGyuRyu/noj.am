s = input()
l = [0] * 26
for i in s:
    l[ord(i) - 97] += 1
for j in l:
    print(j, end=' ')