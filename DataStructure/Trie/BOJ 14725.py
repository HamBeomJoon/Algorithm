# 백준 14725번: 개미굴 (Gold 2)

import sys
input = sys.stdin.readline
class Trie:
    def __init__(self):
        self.root = {}      # 자식저장
    
    def insert(self, food):
        cur_node = self.root

        for string in food:
            if string not in cur_node:
                cur_node[string] = {}
            cur_node = cur_node[string]

        cur_node['*'] = True       # 문자열 마지막에 * 삽입
    
    def print_list(self, cnt, cur_node):
        if '*' in cur_node:
            return

        for child in cur_node:
            print("--" * cnt + child)
            self.print_list(cnt+1, cur_node[child])

trie = Trie()
N = int(input())
food_list = []
for _ in range(N):
    k, *t = map(str,input().split())
    food_list.append(t)

food_list.sort()
for foods in food_list:
    trie.insert(foods)

trie.print_list(0, trie.root)
