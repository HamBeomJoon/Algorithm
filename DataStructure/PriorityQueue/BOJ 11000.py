# 백준 11000번: 강의실 배정(Gold 5)
# '끝나는 시간'기준으로 정렬 한 뒤, 우선순위에 넣고 각 강의의 시작시간과 비교해서 heapq에 넣고빼고를 반복한다.

import sys, heapq
input = sys.stdin.readline
N = int(input())
time, h = [], []
for _ in range(N):
    s, t = map(int,input().split())
    time.append([s, t])

time.sort()
heapq.heappush(h, time[0][1])
for i in range(1, N):
    if time[i][0] < h[0]:
        heapq.heappush(h, time[i][1])
    else:
        heapq.heappop(h)
        heapq.heappush(h, time[i][1])
print(len(h))
