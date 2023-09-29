# 버블정렬

import sys

input = sys.stdin.readline

def swap(a, b):
    return [b, a]

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

for end in range(N-1, 0, -1):
    for i in range(N-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = swap(arr[i], arr[i+1])

for i in arr:
    print(i)
