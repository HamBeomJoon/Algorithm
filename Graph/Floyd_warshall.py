# 플로이드-와샬 O(N^3)

dist = [['inf'] * (n+1) for _ in range(n+1)]
def floyd_warshall():
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if i == j:
                        dist[i][j] = 0
                    else:
                        cost[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
