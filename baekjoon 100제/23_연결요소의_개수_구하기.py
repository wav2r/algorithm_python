# DFS : queue 이용

import sys
input = sys.stdin.readline
from collections import defaultdict;
from collections import deque;

# input
N, M = map(int, input().split())

check = [True, True] + [False for _ in range(N-1)]
edge_dict = defaultdict(set)

for i in range(M):
    a, b = list(map(int, input().split()))
    edge_dict[a].add(b)
    edge_dict[b].add(a)

# queue
queue = deque()
queue.append([1, edge_dict[1]])
answer = 1

while queue:
    now, next = queue.pop()
    for node in next:
        if check[node]:
            continue
        check[node] = True
        queue.append([node, edge_dict[node]])

    if not queue:
        i = 1
        while i <= N and check[i]:
            i = i + 1
        
        if i <= N:
            check[i] = True
            queue.append([i, edge_dict[i]])
            answer += 1

print(answer)