'''
오답 사유: 음수가 들어오는 경우 고려 안함

오류 케이스1 :
4
-5 -1 1 2

=> -1, 2를 더해서 1이 되는 경우 발견 X

오류 케이스2 : 
3
-1 1 2

=> 2번째 인덱스부터 find하기 때문에 1을 발견 X
'''

def answer_problem():
    N = int(input())
    nums = list(map(int, input().split(' ')))
    nums.sort()
    
    find = 2
    answer = 0
    
    while find < N:
        target = nums[find]
        p1, p2 = 0, find-1
        while p1 != p2:
            now = nums[p1] + nums[p2]
            #print(p1, nums[p1], p2, nums[p2], now, target)
            if now == target:
                answer += 1
                p1 = p2
            elif now > target:
                p2 -= 1
            else:
                p1 += 1
        find+=1
    return answer

print(answer_problem())
