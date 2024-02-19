from sys import stdin, stdout
n = int(stdin.readline())
for _ in range(n):
    left, right = 0, 0
    left_tmp = 0
    s = stdin.readline().strip()
    flag = 0
    for i in s:
        if left_tmp < 0:
            stdout.write('NO'+'\n')
            flag = 1
            break
        if i == '(':
            left += 1
            left_tmp += 1
        elif i == ')':
            right += 1
            left_tmp -= 1
    if left == right and flag == 0:
        flag = 0
        stdout.write('YES'+'\n')
    elif flag == 0:
        flag = 0
        stdout.write('NO'+'\n')