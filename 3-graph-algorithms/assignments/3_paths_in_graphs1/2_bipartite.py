#Uses python3

import sys
from collections import deque

def bipartite(adj):
    color = [-1] * len(adj)
    que = deque()
    color[0] = 1
    que.append(0)
    while len(que) != 0:
        u = que.popleft()
        for v in adj[u]:
            if v == u:
                return 0
            if color[v] == -1:
                que.append(v)
                color[v] = 1 - color[u]
            elif color[v] == color[u]:
                return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
