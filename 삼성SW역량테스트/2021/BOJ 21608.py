# 백준 21608번 (Silver 1)
# 2021 상반기 삼성SW역량테스트 기출

from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
m = [[0] * N**2 for _ in range(N**2)]
student_list = defaultdict(list)
for _ in range(N**2):
	student, *s = map(int,input().split())
	student_list[student] = s
dx, dy = [0,0,-1,1], [-1,1,0,0]
 
# 1번조건 check
def first_check(i, j, st):
	cnt = 0
	for x in range(4):
		nx, ny = i + dx[x], j + dy[x]
		if 0 <= nx < N and 0 <= ny < N and m[nx][ny] in student_list[st]:
			cnt += 1
	return cnt
 
# 2번조건 check
def second_check(i, j):
	cnt = 0
	for x in range(4):
		nx, ny = i + dx[x], j + dy[x]
		if 0 <= nx < N and 0 <= ny < N and m[nx][ny] == 0:
			cnt += 1
	return cnt
 
# 만족도 구하는 함수
def happy(i, j):
	cnt = 0
	happy_cnt = [0,1,10,100,1000]
	for x in range(4):
		nx, ny = i + dx[x], j + dy[x]
		if 0 <= nx < N and 0 <= ny < N and m[nx][ny] in student_list[m[i][j]]:
			cnt += 1
	return happy_cnt[cnt]
 
for st in student_list:
	dic = defaultdict(list)
	for i in range(N):
		for j in range(N):
			if m[i][j] == 0:
				dic[first_check(i, j, st)].append((i, j))
    	# dic의 key순으로 내림차순 정렬 -> 좋아하는 학생이 많은 칸 순서대로 정렬됨
	s = sorted(dic.items(), key = lambda x: -x[0])
    	# 1번 조건만족하는 칸이 여러개이면 2번조건으로 넘어감
	if len(dic[s[0][0]]) > 1:
		dic2 = defaultdict(list)
		for i,j in dic[s[0][0]]:
			dic2[second_check(i, j)].append((i, j))
        	# dic2의 key순으로 내림차순 정렬 -> 비어있는 칸이 많은 순서대로 정렬됨
		s = sorted(dic2.items(), key = lambda x: -x[0])
        	# 2번 조건 만족하든 안하든 좌표가 (0, 0) 부터 정렬되어있으므로 첫번째 좌표에 st넣어줌
		m[dic2[s[0][0]][0][0]][dic2[s[0][0]][0][1]] = st
	else:
		m[dic[s[0][0]][0][0]][dic[s[0][0]][0][1]] = st
 
dab = 0
for i in range(N):
	for j in range(N):
		dab += happy(i, j)
print(dab)
