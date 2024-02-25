from collections import deque, defaultdict

N = int(input())
nodes = defaultdict(list)
for node in range(1, N+1):
    arr = list(map(int, input().split()))
    index = 0
    start = arr[index]
    index += 1
    while True:
        end= arr[index]
        if end == -1:
            break
        d = arr[index + 1]
        nodes[start].append((end, d))
        index += 2

distance = [0 for _ in range(N+1)]
visited = [False] * (N+1)

def BFS(start):
    queue = deque()
    
    visited[start] = True
    queue.append(start)

    while queue:
        now = queue.popleft()
        for next_node, next_distance in nodes[now]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                distance[next_node] = distance[now] + next_distance

# 임의의 한 지점에서 최댓값인 지점은
# 지름을 구성하는 두 점 중 하나일 것이라는 아이디어
BFS(1)
Max = 1
for i in range(2, N + 1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (N+1)
visited=[False] * (N+1)
BFS(Max)
distance.sort()
print(distance[N])
