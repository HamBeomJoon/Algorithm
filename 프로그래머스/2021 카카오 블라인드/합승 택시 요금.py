# 1. 플로이드-와샬 (270ms ~ 2300ms)
# 대부분의 케이스에서 2000ms정도가 나왔다.

def solution(n, s, a, b, fares):
    ans = 200000001
    cost = [[20000001] * (n+1) for _ in range(n+1)]
    def floyd_warshall():
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if i == j:
                        cost[i][j] = 0
                    else:
                        cost[i][j] = min(cost[i][k] + cost[k][j], cost[i][j])
        
    for i, j, c in fares:
        cost[i][j] = c
        cost[j][i] = c
    floyd_warshall()
        
    for i in range(1, n+1):
        ans = min(cost[s][i] + cost[i][a] + cost[i][b], ans)
    return ans

# 2. 다익스트라 (15ms ~ 1600ms, 3700ms)
# 대부분의 케이스에서 빠른 속도를 보이지만, 케이스 하나에서 3700ms가 나왔다.
# 간선의 개수가 많아지면 더 느린듯..

import heapq
def solution(n, s, a, b, fares):

    def dijkstra(start):
        res = [float('INF') for _ in range(n+1)]
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

    ans = 200000001
    graph = [[] for _ in range(n+1)]
    for i, j, c in fares:
        graph[i].append((j, c))
        graph[j].append((i, c))
    
    dist = [[]]
    for i in range(1, n+1):
        dist.append(dijkstra(i))

    for i in range(1, n+1):
        ans = min(ans, dist[s][i] + dist[i][a] + dist[i][b])
    return ans
