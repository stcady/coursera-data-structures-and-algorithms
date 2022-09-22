#Uses python3

import sys


def acyclic(adj):
    visited = [False] * len(adj)
    path = [False] * len(adj)
    for v in range(0, len(adj)):
        if not visited[v]:
            if explore(adj, visited, path, v):
                return 1
    return 0

def explore(adj, visited, path, s):
    visited[s] = True
    path[s] = True
    for d in adj[s]:
        if not visited[d]:
            if explore(adj, visited, path, d):
                return True
        elif path[d]:
            return True
    path[s] = False
    return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
