from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M, start = list(map(int, input().split()))
edges = [[] for _ in range(N+1)]

for i in range(M):
    edge = list(map(int, input().split()))
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])

for i in range(N+1):
    edges[i].sort()

visited = [True] + [False for i in range(N)]

def DFS(now):
    print(now, end=' ')
    visited[now] = True
    for target in edges[now]:
        if not visited[target]:
            DFS(target)

DFS(start)

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
        
print()          
visited = [True] + [False for i in range(N)]
BFS(start)
        
