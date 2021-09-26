# 백준 16571: 알파 틱택토(Gold 2)

import sys
sys.setrecursionlimit(10**6)
first, second = 0, 0
blank = []
m = [list(map(int,input().split())) for _ in range(3)]
# 이미 1이 놓여진 칸과 2가 놓여진 칸, 0이 놓여진 칸을 세준다.
for i in range(3):
    for j in range(3):
        if m[i][j] == 1:
            first += 1
        elif m[i][j] == 2:
            second += 1
        elif m[i][j] == 0:
            blank.append([i, j])
 
# check함수: 플레이어 1이나 2중 게임을 끝낸 사람이 있으면 True 리턴, 아니면 False 리턴
def check(m, turn):
    # 현재 턴은 아직 ox를 그리기 전이므로 prev_turn에 이전플레이어 저장해줌.
    prev_turn = 1 if turn == 2 else 2
    if (m[0][0] == m[1][1] == m[2][2] == prev_turn) or (m[0][2] == m[1][1] == m[2][0] == prev_turn):
        return True
    for i in range(3):
        if (m[i][0] == m[i][1] == m[i][2] == prev_turn) or (m[0][i] == m[1][i] == m[2][i] == prev_turn):
            return True
    return False
 
def BT(m, turn):
    # turn이 2 다음에는 3이 아니라 다시 1로 와야한다.
    if turn == 3:
        turn = 1
    mn = 2
    # 만약 저번턴(상대)의 플레이어가 게임을 끝냈다면 -1 return
    if check(m, turn):
        return -1
 
    for i in range(3):
        for j in range(3):
            if m[i][j] == 0:
                m[i][j] = turn
                mn = min(mn, BT(m, turn+1))
                m[i][j] = 0
 
    if mn == 1:
        return -1
    elif mn == 2 or mn == 0:
        return 0
    else:
        return 1
 
# 처음 맵에 1의 개수와 2의 개수가 같다면 플레이어 1 차례, 아니면 플레이어 2 차례
if first == second:
    start = 1
else:
    start = 2
 
# 맵에 0이 없으면 비겼으므로 D출력
if not blank:
    print('D')
    sys.exit(0)
# BT함수에 m, start(시작플레이어) 넣어주고 res에 결과값 저장
res = BT(m, start)
if res == 1:
    print('W')
elif res == 0:
    print('D')
else:
    print('L')
