# 백준 21869번: Maximum Bishop (Silver 2)
# https://kkt89.hatenablog.com/entry/2021/06/23/BOJ-21869_Maximum_Bishop
# 이런 풀이 생각하는 거 보면 진짜 감탄이 나온다..

N = int(input())
if N == 1:
    print(1)
    print(1, 1)
else:
    print(2 * (N-1))
    for i in range(N):
        print(1, i+1)
    for i in range(1, N-1):
        print(N, i+1)
