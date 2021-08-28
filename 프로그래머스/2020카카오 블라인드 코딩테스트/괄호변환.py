# https://hbj0209.tistory.com/168
# 프로그래머스 level 2

def solution(p):
    # 올바른 괄호 문자열인지 판단하는 함수
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
    
    # 문자열의 괄호 방향을 뒤집어서 반환해주는 함수
    def change(s):
        tmp = ''
        for i in s:
            if i == ')':
                tmp += '('
            else:
                tmp += ')'
        return tmp
    
    # p가 이미 올바른 문자열이면 그대로 return, 빈 문자열이면 그대로 return
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
