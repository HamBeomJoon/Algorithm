# 백준 1561: 놀이공원 (Gold 2)

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
rides = list(map(int,input().split()))

def check(m):
    cnt = M
    for r in rides:
        cnt += m // r
    return cnt >= N

if M == 1:
    print(1)
else:
    lo, hi = 1, 60000000000
    while lo != hi:
        mid = (lo + hi) >> 1
        if check(mid):
            hi = mid
        else:
            lo = mid + 1

    if lo == 1:
        print(N)
    else:
        people = M
        for r in rides:
            people += (lo - 1) // r
        
        for i in range(M):
            if lo % rides[i] == 0:
                people += 1
            if people == N:
                print(i + 1)
                break
