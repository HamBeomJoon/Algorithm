# MST: 최소 스패닝 트리
# Union-Find + Prim알고리즘 or Kruskal알고리즘

# 백준 1922번 (네트워크 연결)

import sys
input = sys.stdin.readline

def find(c):
	if par[c] == c:
		return c
	else:
		par[c] = find(par[c])
	return par[c]

def union(a, b):
	a, b = find(a), find(b)
	par[max(a,b)] = min(a,b)

def check(a, b):
	return find(a) == find(b)

N = int(input())
M = int(input())
edge = []
res = 0
par = [i for i in range(N+1)]
for i in range(M):
	a,b,c = map(int,input().split())
	edge.append((c, a, b)) # cost순으로 정렬해줘야 하기 때문에 c,a,b로 저장(sort때문)
edge.sort()
for e in edge:
	c, a, b = e
	if not check(a, b):
		union(a, b)
		res += c
print(res)
