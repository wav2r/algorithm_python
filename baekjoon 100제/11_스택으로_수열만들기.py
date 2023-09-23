# 1874 : Stack

import sys
input = sys.stdin.readline

def answer_problem():
    N = int(input())
    
    stack = [0]
    tmp = [i+1 for i in range(N)]
    tmp.sort(reverse=True)

    answer = []
    
    for _ in range(N):
        find = int(input())
        
        while stack[-1] < find:
            stack.append(tmp.pop())
            answer.append('+')

        if stack[-1] == find:
            stack.pop()
            answer.append('-')
        else:
            return False
    
    return answer

answer = answer_problem()

if answer:
    for ch in answer:
        print(ch)
else:
    print('NO')