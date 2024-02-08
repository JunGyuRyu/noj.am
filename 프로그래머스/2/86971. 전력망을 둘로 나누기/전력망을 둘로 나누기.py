from collections import deque
def solution(n, wires):

    def count_node(n, wires):
        graph = [[False] * (n+1) for _ in range(n+1)]

        for a, b in wires:
            graph[a][b] = True
            graph[b][a] = True

        visit = [False] * (n+1)
        node_num = 0
        queue = deque()
        queue.appendleft(n)
        while queue:
            next_node = queue.pop()
            if visit[next_node]: continue
            visit[next_node] = True
            node_num += 1
            for i in range(1, len(visit)):
                if not graph[next_node][i] : continue
                queue.appendleft(i)
        return node_num

    node_diff = []
    for i in range(len(wires)):
        wires_tmp = wires.copy()
        disconnect = wires_tmp.pop(i)
        node_num1 = count_node(n, wires_tmp)
        node_num2 = n - node_num1
        
        node_diff.append(abs(node_num1 - node_num2))
    return min(node_diff)