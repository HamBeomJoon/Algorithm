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