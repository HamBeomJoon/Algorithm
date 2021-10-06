# 백준 2042번: 구간 합 구하기 (Gold 1)

import sys
input = sys.stdin.readline
# arr: 배열 arr
# tree: 세그먼트 트리
# node: 세그먼트 트리 노드 번호
# node가 담당하는 합의 범위가 start ~ end
def init(arr, tree, node, start, end): 
    # start == end인 경우는 node가 리프노드인 경우, N이 1일때 start = end = 0
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = init(arr, tree, node*2, start, (start+end)//2) + init(arr, tree, node*2+1, (start+end)//2+1, end)
        return tree[node]

# 구간 합 구하기
# node가 담당하고 있는 구간이 [start, end] 이고, 합을 구해야하는 구간이 [left, right]
def getsum(tree, node, start, end, left, right):
    # 1. [left, right]와 [start, end]가 겹치지 않는 경우 0을 리턴해 탐색 종료
    if left > end or right < start:
        return 0
    # 2. [left, right]가 [start, end]를 완전히 포함하는 경우 node의 자식도 모두 포함되기
    # 때문에 더 이상 호출하는 것이 비효율적 -> tree[node]를 리턴해 탐색 종료
    if left <= start and end <= right:
        return tree[node]

    # 3. [start, end]가 [left, right]를 완전히 포함하는 경우
    # 4. [left, right]와 [start, end]가 겹쳐져 있는 경우 (1, 2, 3 제외한 나머지 경우)
    # 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색 시작
    return getsum(tree, node*2, start, (start+end)//2, left, right) + getsum(tree, node*2+1, (start+end)//2+1, end, left, right)

# 수 변경하기
# index번째 수를 val로 변경하는 경우
def update(tree, node, start, end, index, diff):
    # 1. [start, end]에 index가 포함되지 않는 경우 그 자식도 index가 포함되지 않기 때문에 탐색 중단
    if index < start or index > end:
        return
    
    # 2. [start, end]에 index가 포함되는 경우
    tree[node] += diff
    # 리프노드가 아닌 경우 자식도 변경해줘야 하므로 start != end 체크
    if start != end:
        update(tree, node*2, start, (start+end)//2, index, diff)
        update(tree, node*2+1, (start+end)//2+1, end, index, diff)

N, M, K = map(int,input().split())
arr = []
tree = [0] * 10000000
for _ in range(N):
    num = int(input())
    arr.append(num)
init(arr, tree, 1, 0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1:
        b -= 1
        diff = c - arr[b]
        arr[b] = c
        update(tree, 1, 0, N-1, b, diff)
    elif a == 2:                
        print(getsum(tree, 1, 0, N-1, b-1, c-1))
