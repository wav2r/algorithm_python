# 2751

from collections import deque

# merge a1(sort된 상태) a2(sort된 상태)
def merge(a1, a2):
    idx1, idx2 = 0, 0
    result = []
    while idx1 < len(a1) and idx2 < len(a2):
        if a1[idx1] < a2[idx2]:
            result.append(a1[idx1])
            idx1 += 1
        else:
            result.append(a2[idx2])
            idx2 += 1
            
    if idx1 < len(a1):
        result = result + a1[idx1:]
    if idx2 < len(a2):
        result = result + a2[idx2:]
    return result

# arr을 size:1의 배열들로 나눔
def partition(arr):
    result = deque()
    for num in arr:
        result.append([num])
    return result

# merge_sort 실행
def merge_sort(parts):
    count = 0
    while len(parts) > 1:
        arr1 = parts.popleft()
        arr2 = parts.popleft()
        
        parts.append(merge(arr1, arr2))
        count += 1
    return parts


N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

parts = partition(nums)
print(*merge_sort(parts)[0], sep='\n')
