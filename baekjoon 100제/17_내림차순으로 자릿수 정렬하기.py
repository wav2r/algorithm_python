# 1427 : 선택정렬 구현

MIN_NUMBER = -1

def swap(a, b):
    return b, a

arr = list(map(int, input()))
maxIdx = 0
N = len(arr)

for i in range(N):
    maxIdx = i
    for k in range(i, N):
        if arr[maxIdx] < arr[k]:
            maxIdx = k
    arr[i], arr[maxIdx] = swap(arr[i], arr[maxIdx])

for n in arr:
    print(n, end='')
