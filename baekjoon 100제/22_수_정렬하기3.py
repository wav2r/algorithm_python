#기수 정렬 문제
#기수 정렬의 알고리즘을 그대로 구현한 코드 : 메모리 초과

import sys
input = sys.stdin.readline

N = int(input())

count = [0] * 10001

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)