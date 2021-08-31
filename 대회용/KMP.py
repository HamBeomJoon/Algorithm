# 백준 16916: 부분 문자열 (Gold 4)


def make_table():
    table = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
 
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

def KMP():
    table = make_table()
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]
 
        if s[i] == p[j]:
            if j == len(p)-1:
                return True
            else:
                j += 1
    return False
  
s = input()
p = input()
if KMP():
    print(1)
else:
    print(0)
