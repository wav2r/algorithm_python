# 2차원 누적 합

import sys
input = sys.stdin.readline

N, Q = map(int, input().split(' '))
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

# 2차원 배열의 누적합을 구함
def sum_arr(arr):
    tmp = [line for line in arr]

    for i in range(1, N):
        tmp[i][0] += tmp[i-1][0]
        tmp[0][i] += tmp[0][i-1]

    for x in range(1, N):
        for y in range(1, N):
            tmp[x][y] = tmp[x][y] + tmp[x-1][y] + tmp[x][y-1] - tmp[x-1][y-1]
    return tmp

def plus_zero(arr):
    length = len(arr)
    tmp = [[0 for _ in range(length+1)]]
    for line in arr:
        tmp.append([0] + line)
    return tmp

new_arr = plus_zero(sum_arr(arr))

for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split(' '))
    print(new_arr[x2][y2] - new_arr[x2][y1-1] - new_arr[x1-1][y2] + new_arr[x1-1][y1-1])
