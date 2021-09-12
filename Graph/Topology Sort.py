# 백준 2252번: 줄 세우기

from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
	A, B = map(int,input().split())
	graph[A].append(B)
	indegree[B] += 1

def topologySort():
	result = []
	q = deque()
	# 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
	for i in range(1, N+1):
		if not indegree[i]:
			q.append(i)
	
	# 큐가 빌 때까지 반복
	while q:
		# 큐에서 원소 꺼내기
		x = q.popleft()
		result.append(x)
		# 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
		for i in graph[x]:
			indegree[i] -= 1
			if indegree[i] == 0:
				q.append(i)
		print(x, end = ' ')
topologySort()
