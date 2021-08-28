def solution(table, languages, preference):
    tmp, pre = [], []
    answer = {0: 'SI', 1: 'CONTENTS', 2: 'HARDWARE', 3: 'PORTAL', 4: 'GAME'}
    languages_dict = {'PYTHON': 1, 'C': 2, 'C++': 3, 'C#': 4, 'JAVA': 5, 'JAVASCRIPT': 6, 'SQL': 7, 'KOTLIN': 8, 'PHP': 9}
    SI = {1: 2, 2: 0, 3: 0, 4: 1, 5: 5, 6: 4, 7: 3, 8: 0, 9: 0}
    CONTENTS = {1: 3, 2: 0, 3: 1, 4: 0, 5: 4, 6: 5, 7: 2, 8: 0, 9: 0}
    HARDWARE = {1: 3, 2: 5, 3: 4, 4: 0, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0}
    PORTAL = {1: 3, 2: 0, 3: 0, 4: 0, 5: 5, 6: 4, 7: 0, 8: 2, 9: 1}
    GAME = {1: 0, 2: 2, 3: 5, 4: 4, 5: 1, 6: 3, 7: 0, 8: 0, 9: 0}
    
    for i, p in zip(languages, preference):
        tmp.append([languages_dict[i], p])

    for i in (SI, CONTENTS, HARDWARE, PORTAL, GAME):
        pref_sum = 0
        for l in tmp:
            pref_sum += i[l[0]] * l[1]
        pre.append(pref_sum)
    
    ans = []
    for i in range(5):
        if pre[i] == max(pre):
            ans.append(answer[i])
    ans.sort()
    return ans[0]