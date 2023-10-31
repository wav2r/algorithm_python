# 1517
import sys
input = sys.stdin.readline
result = 0

def merge_sort(start, end):
    global result
    if end - start < 1:
        return
    mid = (end + start) // 2
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    # tmp에 arr copy
    for i in range(start, end + 1):
        tmp[i] = arr[i]

    k = start
    index1 = start
    index2 = mid + 1
    while index1 <= mid and index2 <= end:
        if tmp[index1] > tmp[index2]:
            arr[k] = tmp[index2]
            # 우측 배열의 값을 좌측으로 옮길 떄 result를 더한다
            result = result + index2 - k
            k += 1
            index2 += 1
        else:
            arr[k] = tmp[index1]
            k += 1
            index1 += 1

    while index1 <= mid:
        arr[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= end:
        arr[k] = tmp[index2]
        k += 1
        index2 += 1
        
N = int(input())
arr = list(map(int, input(). split()))
arr.insert(0, 0)
tmp = [0] * (N + 1)
merge_sort(1, N)
print(result)
