from sys import stdin
num_len = int(stdin.readline())
count_dict = dict()

for i in range(num_len):
    num = int(stdin.readline());
    if num not in count_dict:
        count_dict[num] = 1
    else:
        count_dict[num] += 1

sorted_dict = dict(sorted(count_dict.items()))
print(sorted(sorted_dict.items(), key = lambda x: x[1], reverse=True)[0][0])
