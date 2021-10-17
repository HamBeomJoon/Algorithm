# 백준 1756번: 피자 굽기

import sys
input = sys.stdin.readline
D, N = map(int,input().split())
oven = list(map(int,input().split()))
pizza = list(map(int,input().split()))
# 오븐 깊이가 깊은 곳의 반지름은 그 위보다 항상 같거나 작게 재정렬
for i in range(D-1):
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]
 
# cur: 현재 우리가 확인하고자 하는 피자 인덱스
cur = 0
for i in range(D-1, -1, -1):
    # 현재피자의 반지름이 oven의 반지름보다 크면 continue 해줌으로써 i가 다음 오븐반지름 가리킴
    if pizza[cur] > oven[i]:
        continue
    
    # 현재피자의 반지름이 oven[i]의 반지름보다 같거나 작으면 cur 1증가, 다음 피자확인
    # cur이 N이면 모든피자를 오븐에 다 넣은 것이므로 i+1출력
    cur += 1
    if cur >= N:
        print(i+1)
        sys.exit(0)
 
# i가 0까지 왔는데 sys.exit(0)에 걸리지 않았으면 모든 피자를 넣은 것이 아니므로 0출력
print(0)
