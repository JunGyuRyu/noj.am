from sys import stdin, stdout
from collections import deque

input = lambda: stdin.readline().rstrip()
print = stdout.write

N = int(input())
M = int(input())

graph = [[False] * (N+1) for _ in range(N+1)]
infected = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(visit):
    stack = deque()
    stack.append(1) # 1에서 시작
    while stack:
        next_node = stack.pop()
        if visit[next_node]:
            continue
        visit[next_node] = True
        infected.append(next_node)
        for i in range(len(visit)-1, 0, -1):
            if not graph[next_node][i]:
                continue
            stack.append(i)
    return infected

infected = dfs([False] * (N+1))
print(str(len(infected) - 1))