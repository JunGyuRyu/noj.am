from sys import stdin
student_num = [list(map(str,stdin.readline().split())) for i in range(int(input()))]
k = 1
while True:
    tmp = [num[0][-k::] for num in student_num]
    if len(set(tmp)) == len(student_num):
        print(k)
        break
    else:
        k += 1