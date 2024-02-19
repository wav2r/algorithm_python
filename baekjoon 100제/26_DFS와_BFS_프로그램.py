# 기본적인 DFS, BFS 구현

from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M, start = list(map(int, input().split()))
edges = [[] for _ in range(N+1)]

for i in range(M):
    edge = list(map(int, input().split()))
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])

for targets in edges:
    targets.sort()

visited = [True] + [False for i in range(N)]

def DFS(now):
    print(now, end=' ')
    visited[now] = True
    for target in edges[now]:
        if not visited[target]:
            DFS(target)

DFS(start)
print()

def BFS(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for target in edges[now]:
            if not visited[target]:
                visited[target] = True
                q.append(target)
            
                
visited = [True] + [False for i in range(N)]
BFS(start)