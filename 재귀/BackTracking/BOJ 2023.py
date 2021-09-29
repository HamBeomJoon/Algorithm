# 백준 2023번: 신기한 소수 (Gold 5)
# 메모리가 작아 에라토스테네스의 체를 사용하면 MLE를 받는다

import math
def prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

def BT(n):
    if len(str(n)) == N:
        print(n)
    else:
        for i in range(1, 10, 2):
            tmp = n * 10 + i
            if prime(tmp):
                BT(tmp)

N = int(input())
for i in [2, 3, 5, 7]:
    BT(i)
