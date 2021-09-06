def solution(weights, head2head):
    answer = []
    # WL = [[승리횟수, 자신보다 몸무게가 무거운 복서 이긴횟수], 복서번호]
    # 4번째 조건인 작은 번호가 앞에 오도록 하기위해 i+1(복서번호)을 넣어주었다.
    WL = [[[0, 0], i+1] for i in range(len(weights))]

    for h in range(len(head2head)):
        cnt = 0
        for idx, res in enumerate(head2head[h]):
            # 비겼으면 cnt 1증가
            if res == 'N':
                cnt += 1
            if res == 'W':
                # 현재 h번 복서가 idx번 복서를 이기고 몸무게가 작다면
                # 자신보다 몸무게가 무거운 복서를 이겼으므로 WL[h][0][0], WL[h][0][1] 둘다 1 증가
                if weights[idx] > weights[h]:
                    WL[h][0][0] += 1
                    WL[h][0][1] += 1
                else:
                    WL[h][0][0] += 1
        
        # cnt가 len(weights)와 같다면 모든 사람과 붙어본 적이 없으므로 WL[h][0][0] = 0
        # 안그러면 ZeroDivisionError가 뜬다.
        if cnt == len(weights):
            WL[h][0][0] = 0
        else:
            # 붙어본 사람이 1명이상이면 WL[h][0][0]에 승률을 넣어준다.
            # len(weights) 에서 붙어본적이 없는 횟수(cnt)를 빼주면 총 경기수
            # 승률 = 승리횟수 / 총 경기수
            WL[h][0][0] = WL[h][0][0] / (len(weights) - cnt)

    # WL을 정렬해준다. 정렬기준은 다음과 같다.
    # 1. -x[0][0] (승률기준으로 내림차순)
    # 2. -x[0][1](자신보다 몸무게가 무거운 복서 이긴횟수 내림차순)
    # 3. weights[x[1]-1] (복서들의 몸무게 내림차순)
    WL.sort(key = lambda x: (-x[0][0], -x[0][1], -weights[x[1]-1]))
    for i in WL:
        answer.append(i[1])
    return answer
