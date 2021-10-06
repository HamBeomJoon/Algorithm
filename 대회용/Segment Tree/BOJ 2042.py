import sys
input = sys.stdin.readline
def init(arr, tree, node, start, end): 
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = init(arr, tree, node*2, start, (start+end)//2) + init(arr, tree, node*2+1, (start+end)//2+1, end)
        return tree[node]

# 구간 합 구하기
def getsum(tree, node, start, end, left, right): 
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    return getsum(tree, node*2, start, (start+end)//2, left, right) + getsum(tree, node*2+1, (start+end)//2+1, end, left, right)
 
# 값 update 
def update(tree, node, start, end, index, diff):
    if index < start or index > end:
        return
    
    tree[node] += diff
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
