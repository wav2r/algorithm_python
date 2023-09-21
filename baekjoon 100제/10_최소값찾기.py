from collections import deque

def answer_problem():

    N, L = list(map(int, input().split(' ')))
    nums = list(map(int, input().split(' ')))
    tmp = deque()
    
    for i in range(N):
        while tmp and tmp[-1][0] > nums[i]:
            tmp.pop()

        tmp.append((nums[i], i))

        if tmp[0][1] < i - L + 1:
            tmp.popleft()

        print(tmp[0][0], end = ' ')
    return 

answer_problem()
