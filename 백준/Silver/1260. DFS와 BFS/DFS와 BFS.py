from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# DFS
def dfs2(node, visit):
    stack = deque()
    stack.append(node)
    while stack:
        next_node = stack.pop()
        if visit[next_node]: continue
        visit[next_node] = True
        print(next_node, end=' ')
        for i in range(len(visit)-1, 0, -1):
            if not graph[next_node][i]: continue
            stack.append(i)

# BFS
def bfs(node, visit):
    queue = deque()
    queue.appendleft(node)
    while queue:
        next_node = queue.pop()
        if visit[next_node]: continue
        visit[next_node] = True
        print(next_node, end=' ')
        for i in range(1, len(visit)):
            if not graph[next_node][i] : continue
            queue.appendleft(i)

dfs2(V, [False] * (N+1))
print()
bfs(V, [False] * (N+1))