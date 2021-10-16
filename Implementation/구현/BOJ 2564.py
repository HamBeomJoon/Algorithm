# 백준 2564번: 경비원 (Silver 1)
# 그냥 모든 경우를 다 나누어 주었다. 
#상점의 위치와 동근이의 위치가 마주보고 있을때만 추가로 케이스를 2개로 나누어주었다

import sys
input = sys.stdin.readline
w, h = map(int,input().split())
n = int(input())
xlist, ylist = [], []
def solve(xlist, ylist):
    answer = 0
    for i in range(n):
        if sx == xlist[i]:
            answer += abs(sy - ylist[i])
        elif (sx, xlist[i]) == (1, 2) or (sx, xlist[i]) == (2, 1):
            if sy + ylist[i] < w:
                answer += sy + ylist[i] + h
            else:
                answer += w-sy + w-ylist[i] + h
        elif (sx, xlist[i]) == (3, 4) or (sx, xlist[i]) == (4, 3):
            if sy + ylist[i] < h:
                answer == sy + ylist[i] + w
            else:
                answer += h-sy + h-ylist[i] + w
        elif (sx, xlist[i]) == (1, 3) or (sx, xlist[i]) == (3, 1):
            answer += sy + ylist[i]
        elif (sx, xlist[i]) == (1, 4):
            answer += w-sy + ylist[i]
        elif (sx, xlist[i]) == (4, 1):
            answer += sy + w-ylist[i]
        elif (sx, xlist[i]) == (2, 3):
            answer += sy + h-ylist[i]
        elif (sx, xlist[i]) == (3, 2):
            answer += h-sy + ylist[i]
        elif (sx, xlist[i]) == (2, 4) or (sx, xlist[i]) == (4, 2):
            answer += w-sy + h-ylist[i]

    return answer
for _ in range(n):
    x, y = map(int,input().split())
    xlist.append(x)
    ylist.append(y)
sx, sy = map(int,input().split())
print(solve(xlist, ylist))
