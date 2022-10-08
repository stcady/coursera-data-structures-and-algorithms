#Uses python3

import sys
import heapq
import math

def distance(adj, cost, s, t):
    dist = [math.inf] * len(adj)
    prev = [None] * len(adj)
    pq = []
    dist[s] = 0
    heapq.heappush(pq, (0, s))
    while len(pq) != 0:
        _, u = heapq.heappop(pq)
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                prev[v] = u
                dist[v] = dist[u] + cost[u][i]
                heapq.heappush(pq, (dist[v], v))
    if dist[t] == math.inf:
        return -1
    else:
        return dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
