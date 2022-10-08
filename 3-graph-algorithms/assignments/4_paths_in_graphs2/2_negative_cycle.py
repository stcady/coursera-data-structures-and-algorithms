#Uses python3

import sys
import math
import heapq


def negative_cycle(adj, cost):
    v = len(adj)
    dist = [0] * v
    dist[0] = 0
    for i in range(0, v):
        for j in range(0, v):
            for k in adj[j]:
                vi = adj[j].index(k)
                if dist[k] > dist[j] + cost[j][vi]:
                    dist[k] = dist[j] + cost[j][vi]
                    if i == v-1:
                        return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
