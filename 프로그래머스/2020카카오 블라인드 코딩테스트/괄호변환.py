def solution(p):
    def check(s):
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    stack.pop()
        
        return not stack
    
    def change(s):
        tmp = ''
        for i in s:
            if i == ')':
                tmp += '('
            else:
                tmp += ')'
        return tmp
    
    if check(p):
        return p
    if len(p) == 0:
        return ''

    answer = ''
    mx = len(p)
    # 짝수개 단위로 u를 끊어보자
    for i in range(2, mx+1, 2):
        u = p[ :i]
        v = p[i: ]
        
        if u.count(')') == u.count('('):
            if check(u):
                # 균형잡힌 문자열이고 올바른 문자열이면 v 1단계부터 수행
                answer += u
                answer += solution(v)
            else:
                new_s = '(' + solution(v) + ')'
                uu = u[1:-1]
                new_s += change(uu)
                answer += new_s
            return answer

    return answer