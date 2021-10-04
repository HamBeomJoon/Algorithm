import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
t = N
while t > 3:
    if A[0] >= A[N-1]:
        A[0] -= 1
    else:
        A[N-1] -= 1
    t -= 1

A[0] -= 1
A[N-1] -= 1
print(max(A[0], A[N-1]))
