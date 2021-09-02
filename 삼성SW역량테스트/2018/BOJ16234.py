# 2018년도 하반기 기출
# 시뮬레이션 + BFS
# 나는 BFS로 주변 칸과 차이를 비교해주었고, 연합인 나라끼리 union해줘서 union-find로 풀 수도 있다.

import sys
from collections import defaultdict, deque
input = sys.stdin.readline
N, L, R = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
q = deque()
 
def bfs(i, j):
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y+ dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(m[nx][ny] - m[x][y]) <= R:
                    move[len(move)].append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = True
    
    if len(move[len(move)]) == 1:
        del move[len(move)]
 
day = 0
while True:
    move = defaultdict(list)
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                move[len(move) + 1].append((i, j))
                bfs(i, j)
 
    if not move:
        print(day)
        break
    else:
    	# 인구 이동
        for i in move:
            s = 0
            for x, y in move[i]:
                s += m[x][y]
            s = int(s / len(move[i]))
            for x, y in move[i]:
                m[x][y] = s
        day += 1
