def solution(word):
    dic = []
    def add_word(s):
        if len(s) == 6:
            return
        dic.append(s)
        
        for i in ('A', 'E', 'I', 'O', 'U'):
            add_word(s + i)
    
    for i in ('A', 'E', 'I', 'O', 'U'):
        add_word(i)

    return dic.index(word) + 1
