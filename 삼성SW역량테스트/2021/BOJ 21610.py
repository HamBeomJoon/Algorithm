# 2021년 상반기 삼성SW역량테스트 기출문제이다.
# 백준 21610번: 마법사 상어와 비바라기 (Gold 5)
# 상어 초등학교보다 쉬운거같은데.. 상어초등학교가 골드5가 되야할듯.

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
m = [list(map(int,input().split())) for _ in range(N)]
# 물복사버그 함수: 대각선 방향으로 맵을 벗어나지 않는 칸에 물이 존재하면 cnt 1증가
def check(i, j):
    cnt = 0
    if 0 <= i-1 < N and 0 <= j-1 < N and m[i-1][j-1]:
        cnt += 1
    if 0 <= i-1 < N and 0 <= j+1 < N and m[i-1][j+1]:
        cnt += 1
    if 0 <= i+1 < N and 0 <= j-1 < N and m[i+1][j-1]:
        cnt += 1
    if 0 <= i+1 < N and 0 <= j+1 < N and m[i+1][j+1]:
        cnt += 1
    return cnt

def move(d, s, cloud):
    clouds = []
    if cloud == -1:
        cloud = [[N-2, 0], [N-1, 0], [N-1, 1], [N-2, 1]]

    # 1단계: 모든 구름이 d방향으로 s칸 이동한다
    for i, j in cloud:
        nx, ny = (i + dx[d] * s) % N, (j + dy[d] * s) % N
        clouds.append((nx, ny))

    # 2단계: 각 구름에서 비가 내려 구름이 있는 칸 1증가
    for i, j in clouds:
        m[i][j] += 1
    # 3,4단계: 구름이 사라지고 물이 증가한 칸에서 물복사버그 마법을 시전한다.
    for i, j in clouds:
        m[i][j] += check(i, j)
    
    # 5단계: m에서 물의 양이 2이상인 모든칸을 cloud에 넣어주고, 물의 양 2줄어든다.
    cloud = []
    for i in range(N):
        for j in range(N):
            # 이때 구름이 생기는 칸은 3단계에서 사라진 칸이 아니어야 한다.
            if (i, j) not in clouds and m[i][j] >= 2:
                cloud.append((i, j))
                m[i][j] -= 2
    return cloud

cloud = -1
for _ in range(M):
    d, s = map(int,input().split())
    cloud = move(d-1, s, cloud)

# M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합 = answer
answer = 0
for i in range(N):
    for j in range(N):
        answer += m[i][j]
print(answer)
