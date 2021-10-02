# 백준 20003번: 거스름돈이 싫어요 (Silver 1)

import fractions, sys
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
a, b = map(int,input().split())
tmp = fractions.Fraction(a, b)
if N == 1:
    print(tmp.numerator, tmp.denominator)
    sys.exit(0)
g, l = tmp.numerator, tmp.denominator
for _ in range(N-1):
    a, b = map(int,input().split())
    tmp = fractions.Fraction(a, b)
    g = gcd(g, tmp.numerator)
    l = lcm(l, tmp.denominator)

print(g, l)
