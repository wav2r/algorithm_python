from collections import deque
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
maps = []

for j in range(N):
    maps.append([])
    temp = input()
    for i in range(M):
        maps[j].append(int(temp[i]))

queue = deque()
queue.append([0, 0])

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[False] * M for _ in range(N)]
visited[0][0] = True

while queue:
    x, y = queue.popleft()
    for direction in directions:
        dx, dy = direction
        nx, ny = x + dx, y + dy
        if nx < 0 or nx > M - 1 or ny < 0 or ny > N - 1:
            continue
        if maps[ny][nx] and not visited[ny][nx]:
            visited[ny][nx] = True
            maps[ny][nx] = maps[y][x] + 1
            queue.append((nx, ny))

print(maps[N-1][M-1])