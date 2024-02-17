s = input()
l = ['-1'] * 26
for i, j in enumerate(s):
    tmp = 25-(122-ord(j))
    if l[tmp] == '-1':
        l[tmp] = str(i)
print(' '.join(l))