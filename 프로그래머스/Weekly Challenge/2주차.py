def solution(scores):
    answer = ''
    score_sum = []
    for i in range(len(scores)):
        s = []
        for j in range(len(scores)):
            s.append(scores[j][i])
        target = scores[i][i]
        if (max(s) == target and s.count(target) == 1) or (min(s) == target and s.count(target) == 1):
            score_sum.append([sum(s) - target, len(scores) - 1])
        else:
            score_sum.append([sum(s), len(scores)])
    
    for i in score_sum:
        if i[0] / i[1] >= 90:
            answer += 'A'
        elif i[0] / i[1] >= 80:
            answer += 'B'
        elif i[0] / i[1] >= 70:
            answer += 'C'
        elif i[0] / i[1] >= 50:
            answer += 'D'
        elif i[0] / i[1] < 50:
            answer += 'F'
    return answer