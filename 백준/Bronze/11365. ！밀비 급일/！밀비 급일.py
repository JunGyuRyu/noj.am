from sys import stdin, stdout
l = []
while True:
    s = stdin.readline().strip()
    if s == "END":
        break 
    l.append(s)
for i in l:
    stdout.write(i[::-1] + '\n')