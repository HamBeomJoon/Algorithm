# a, b사이의 소수 구하기

import math
def get_primes(a, b):
    is_primes = [True] * b
    max_length = math.ceil(math.sqrt(b))
    for i in range(2, max_length):
        if is_primes[i]:
            for j in range(i+i, b, i):
                is_primes[j] = False
    return [i for i in range(a, b) if is_primes[i]]
