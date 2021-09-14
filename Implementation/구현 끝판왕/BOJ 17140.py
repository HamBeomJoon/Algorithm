# BOJ 17140: 이차원 배열과 연산 (Gold 4)
# Counter함수를 사용하면 훨씬 짧은 코드로 풀 수 있다.

import sys, copy
from collections import defaultdict
input = sys.stdin.readline
r, c, k = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(3)]
time = 1
if (r-1 < len(m) and c-1 < len(m[0])) and m[r-1][c-1] == k:
    print(0)
else:
    while True:
        row, col = len(m), len(m[0])
        new_arr = [] 
        if row >= col:
            # R 연산
            max_length = 0
            for i in m:
                tmp = []
                count = defaultdict(int)
                
                for j in i:
                    if j == 0:
                        continue
                    count[j] += 1

                sort_arr = sorted(count.items(), key=lambda x: (x[1], x[0]))
                if len(count.items()) > max_length:
                    max_length = len(count.items())

                for j in sort_arr:
                    tmp.extend((j[0], j[1]))
                new_arr.append(tmp[:100])

            for i in new_arr:
                if len(i) < max_length * 2:
                    zero = [0] *(max_length * 2 - len(i))
                    i.extend(zero)
            
            m = copy.deepcopy(new_arr)
        
        else:
            # C 연산
            max_length = 0
            for i in range(len(m[0])):
                tmp = []
                count = defaultdict(int)
                
                for j in range(len(m)):
                    if m[j][i] == 0:
                        continue
                    count[m[j][i]] += 1

                sort_arr = sorted(count.items(), key=lambda x: (x[1], x[0]))
                if len(count.items()) > max_length:
                    max_length = len(count.items())

                for j in sort_arr:
                    tmp.extend((j[0], j[1]))
                new_arr.append(tmp[:100])

            for i in new_arr:
                if len(i) < max_length * 2:
                    zero = [0] *(max_length * 2 - len(i))
                    i.extend(zero)

            tmp2 = [[0] * len(new_arr) for _ in range(len(new_arr[0]))]
            for i in range(len(new_arr)):
                for j in range(len(new_arr[0])):
                    tmp2[j][i] = new_arr[i][j]
            
            m = copy.deepcopy(tmp2)

        if (r-1 < len(m) and c-1 < len(m[0])) and m[r-1][c-1] == k:
            print(time)
            break
        
        time += 1
        if time > 100:
            print(-1)
            break
