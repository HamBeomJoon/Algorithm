def solution(s):
    if len(s) == 1:
        return 1
    mx = len(s) // 2
    dab = 2001
    for i in range(1, mx+1):
        answer = ''
        target = s[ :i]
        cnt = 1
        for j in range(i, len(s), i):
            new_s = s[j: j+i]
            if new_s == target:
                cnt += 1
            else:
                if cnt == 1:
                    answer += target
                else:
                    answer += str(cnt) + target
    
                target = new_s
                cnt = 1
            
        if cnt == 1:
            answer += target
        else:
            answer += str(cnt) + target
            
        dab = min(dab, len(answer))
        
    return dab