import re
def solution(new_id):

    # 1단계
    s = new_id.lower()
    # 2단계
    s = re.sub('[^a-zA-Z0-9\-_.]', '', s)
    # 3단계
    s = re.sub('\.{2,}', '.', s)
    # 4단계
    if len(s) > 0 and s[0] == '.':
        s = s[1: ]
    if len(s) > 0 and s[-1] == '.':
        s = s[ :-1]
    # 5단계
    if len(s) == 0:
        s = 'a'
    # 6단계
    if len(s) >= 16:
        s = s[ :15]
    if s[-1] == '.':
        s = s[ :-1]
    # 7단계
    if len(s) <= 2:
        while len(s) < 3:
            s += s[-1]
            
    return s
