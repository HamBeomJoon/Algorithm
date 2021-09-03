# 정확성은 통과했지만, 효율성에서 시간초과가 발생한다.
# 인터넷에 있는 풀이말고는 안되는 건가..

from collections import defaultdict
def solution(info, query):
    dic = defaultdict(set)
    answer = [0] * len(query)
    for i in range(len(info)):
        sinfo = info[i].split(" ")
        dic[i+1] = [{sinfo[0], sinfo[1], sinfo[2], sinfo[3]}, int(sinfo[4])]

    for idx, q in enumerate(query):
        sq = q.split(" ")
        
        for d in dic:
            cnt = 0    
            for i in sq:
                if i == '-' or i in dic[d][0]:
                    cnt += 1
            
            if cnt == 4 and int(sq[7]) <= dic[d][1]:
                answer[idx] += 1
            
    return answer
