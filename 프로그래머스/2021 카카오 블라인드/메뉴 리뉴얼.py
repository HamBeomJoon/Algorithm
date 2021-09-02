# Counter함수 공부하자!

from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    
    for i in course:
        c = []
        for menu_li in orders:
            for li in combinations(menu_li, i):
                res = ''.join(sorted(li))
                c.append(res)
        all_menu = Counter(c).most_common()
    
        ans = [[0, 0]]
        for a in all_menu:
            if a[1] > ans[0][1]:
                ans = [[a[0], a[1]]]
            elif a[1] == ans[0][1]:
                ans.append([a[0], a[1]])

        for i in ans:
            if i[1] > 1:
                answer.append(i[0])

    return sorted(["".join(s) for s in map(sorted, answer)])
