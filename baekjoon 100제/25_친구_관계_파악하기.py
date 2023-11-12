# DFS - 재귀 방식
# exit() 사용
# 700ms

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
        print(1)
        exit()
    
    visited[now] = True
    for next in edges[now]:
        if not visited[next]:
            dfs(next, count + 1)
    visited[now] = False

# main
answer = 0
for start in range(N):
    dfs(start, 0)

print(0)