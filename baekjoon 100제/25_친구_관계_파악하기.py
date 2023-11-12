# DFS - 재귀 방식
# visited를 변경하는 시점을 변경
# 1200ms

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = list(map(int, input().split()))

visited = [False] * (N + 1)

# input
edges = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

# dfs function
def dfs(now, count):
    global answer

    if count == 4:
        answer = 1
        return
    
    visited[now] = True
    for next in edges[now]:
        if not visited[next]:
            dfs(next, count + 1)
    visited[now] = False

# main
answer = 0
for start in range(N):
    dfs(start, 0)

    if answer:
        break 

print(answer)