# DFS
# 시간초과 발생

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
from collections import defaultdict;

N, M = list(map(int, input().split()))

# input
edges = list()
edge_dict = defaultdict(set)

for i in range(M):
    a, b = list(map(int, input().split()))
    edges.append([a, b])
    edge_dict[a].add(b)
    edge_dict[b].add(a)

def switch_ans():
    global answer
    answer = 1

# dfs function
def dfs(now, chk, count):
    if count == 4:
        switch_ans()
        return

    for next in edge_dict[now]:
        if chk[next]:
            continue

        dfs(next, chk[:next] + [True] + chk[next+1:], count + 1)

# main
answer = 0
for start in range(N):
    dfs(start, [True]+[0 for _ in range(N-1)], 0)

    if answer == 1:
        break 

print(answer)