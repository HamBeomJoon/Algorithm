# 백준 5525번: IOIOI (Silver 2)
# 단순히 문자열 M을 한번만 돌며 갯수를 count하는 O(M)방법이 더 빠르다.
# KMP공부하기 위해 일부러 kmp로 풀었다.

def make_table(p):
    table = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
 
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

def KMP(p):
    table = make_table(p)
    cnt = 0
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]
 
        if s[i] == p[j]:
            if j == len(p)-1:
                cnt += 1
                j = table[j]
            else:
                j += 1
    
    return cnt

N = int(input())
M = int(input())
s = input()
target = 'IO' * N + 'I'
ans = KMP(target)
print(ans)
