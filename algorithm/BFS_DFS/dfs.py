# dfs 구현 방법 2가지
graph = dict({1: [2, 3, 8], 2: [1, 4, 5], 3: [1, 6],
              4: [2], 5: [2], 6: [3, 7], 7: [6], 8: [1]})
# 재귀 이용
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

dfs_order = recursive_dfs(1)
print(dfs_order)

# 반복문 이용
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v= stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

dfs_order = iterative_dfs(1)

print(dfs_order)
