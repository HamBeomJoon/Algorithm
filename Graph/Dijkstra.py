# 다익스트라 O(ElogV)

import heapq
def dijkstra(start):
    res = [float('INF') for _ in range(V)]
    res[start] = 0
    q = []
    heapq.heappush(q, (res[start], start))
    while q:
        result_x, x = heapq.heappop(q)
        for fu, fw in graph[x]:
            if res[fu] > result_x + fw:
                res[fu] = result_x + fw
                heapq.heappush(q, ([res[fu], fu]))
    return res
