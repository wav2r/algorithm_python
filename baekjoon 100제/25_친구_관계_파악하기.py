# DFS - 재귀 방식
# 1500ms

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = list(map(int, input().split()))

visited = [False] * (N + 1)

# input
edge_dict = [[] for _ in range(N)]

for i in range(M):
    a, b = list(map(int, input().split()))
    edge_dict[a].append(b)
    edge_dict[b].append(a)

# dfs function
def dfs(now, count):
    global answer
    
    if count == 4:
        answer = 1
        return

    for next in edge_dict[now]:
        if visited[next]:
            continue
        visited[next] = True
        dfs(next, count + 1)
        visited[next] = False

# main
answer = 0
for start in range(N):
    visited[start] = True
    dfs(start, 0)
    visited[start] = False

    if answer == 1:
        break 

print(answer)