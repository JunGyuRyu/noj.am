from sys import stdout

L, P = map(int, input().split())
nums = list(map(int, input().split()))
for n in nums:
    stdout.write(str(n - (L*P)) + ' ')