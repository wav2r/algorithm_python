# 17298 : 오큰수 구하기

import sys
input = sys.stdin.readline

def answer_problem():
    N = int(input())
    arr = list(map(int, input().split(' ')))

    stack = []
    answer = [0 for _ in range(N)]

    for i in range(N):
        while stack and arr[stack[-1]] < arr[i]:
            answer[stack.pop()] = arr[i]
            
        stack.append(i)

    while stack:
        answer[stack.pop()] = -1
    
    return answer

answer = answer_problem()

for n in answer:
    print(n, end= ' ')
