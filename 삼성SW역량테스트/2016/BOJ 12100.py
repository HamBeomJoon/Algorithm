# 백준 12100번: 2048(Easy)
# 2016년 하반기 기출 (Gold 2)
# 백트래킹 + 시뮬레이션 (빡구현)

import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
mx = 0
block = [list(map(int,input().split())) for _ in range(N)]
# dir : 상 하 좌 우 / 1 2 3 4
def recur(dir):
 
    if dir == 1:
        for i in range(N):
            p = []
            for j in range(N):
                if block[j][i] != 0:
                    p.append(block[j][i])
 
            p += [0] * (N - len(p))
            for j in range(N):
                block[j][i] = p[j]
        
        for i in range(N-1):
            for j in range(N):
                if block[i+1][j] == block[i][j]:
                    block[i][j] = block[i+1][j] * 2
                    for k in range(i+1, N-1):
                        block[k][j] = block[k+1][j]
                    block[-1][j] = 0
 
    if dir == 2:
        for i in range(N):
            p = []
            for j in range(N):
                if block[j][i] != 0:
                    p.append(block[j][i])
 
            p = [0] * (N - len(p)) + p
            for j in range(N):
                block[j][i] = p[j]
 
        for i in range(N-1, 0, -1):
            for j in range(N):
                if block[i][j] == block[i-1][j]:
                    block[i][j] = block[i-1][j] * 2
                    for k in range(i-1, 0, -1):
                        block[k][j] = block[k-1][j]
                    block[0][j] = 0
 
    if dir == 3:
        for i in range(N):
            p = []
            for j in range(N):
                if block[i][j] != 0:
                    p.append(block[i][j])
 
            p += [0] * (N - len(p))
            for j in range(N):
                block[i][j] = p[j]
                        
        for i in range(N):
            for j in range(N-1):
                if block[i][j] == block[i][j+1]:
                    block[i][j] = block[i][j] * 2
                    for k in range(j+1, N-1):
                        block[i][k] = block[i][k+1]
                    block[i][-1] = 0
 
    if dir == 4:
        for i in range(N):
            p = []
            for j in range(N):
                if block[i][j] != 0:
                    p.append(block[i][j])
 
            p = [0] * (N - len(p)) + p
            for j in range(N):
                block[i][j] = p[j]
 
        for i in range(N):
            for j in range(N-1, 0, -1):
                if block[i][j] == block[i][j-1]:
                    block[i][j] = block[i][j-1] * 2
                    for k in range(j-1, 0, -1):
                        block[i][k] = block[i][k-1]
                    block[i][0] = 0
 
def BT(cnt):
    global block, mx
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                if block[i][j] > mx:
                    mx = block[i][j]
        return
 
    b = copy.deepcopy(block)
    for i in range(1, 5):
        recur(i)
        BT(cnt+1)
        block = copy.deepcopy(b)
 
BT(0)
print(mx)
