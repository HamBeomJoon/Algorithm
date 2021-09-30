# 백준 19637번: IF문 좀 대신 써줘

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
ss, power = [], []
for _ in range(N):
    s, p = map(str,input().split())
    power.append(int(p))
    ss.append(s)

def binary_search(n):
    lo, hi = 0, len(power) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if power[mid] < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return ss[hi + 1]

for _ in range(M):
    num = int(input())
    print(binary_search(num))
