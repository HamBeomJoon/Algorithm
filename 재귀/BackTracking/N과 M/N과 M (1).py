# BOJ 15649: N과 M(1) 
# Silver 3

N, M = map(int,input().split())
answer = []
def BT(length, comb):
	if length == M:
		answer.append(comb.copy())
		return
	
	for i in range(1, N + 1):
		if i in comb:
			continue
		comb.append(i)
		BT(length + 1, comb)
		comb.pop()

	return answer

BT(0, [])
for i in answer:
	print(*i)
