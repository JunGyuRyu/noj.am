from sys import stdin
import math

ch_now = 100
ch_des = int(input().strip()) # 5457
broken_num = int(input().strip()) # 3

broken_btn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

tmp_btn = []
if broken_num != 0:
    tmp_btn = list(map(int, stdin.readline().strip().split(" "))) # 6 7 8

if len(tmp_btn) != 0:
    for i in tmp_btn:
        broken_btn[i] = 1

channels = []
for i in range(1000000):
    flag = 0
    for s in str(i):
        if broken_btn[int(s)] == 1:
            flag += 1
            break
    if flag == 0:
        channels.append(i)


if broken_btn.count(1) != 10:
    dis = abs(min(channels, key=lambda x: abs(x-ch_des)) - ch_des)
    num = min(channels, key=lambda x: abs(x-ch_des))
    if dis + len(str(num)) > abs(ch_des - 100):
        print(abs(ch_des - 100))
    else:
        print(dis + len(str(num)))
else:
    print(abs(ch_des - 100))