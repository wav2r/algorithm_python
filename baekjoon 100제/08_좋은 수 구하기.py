'''
서로 다른 두 수의 합으로 표현되는 수가 있다면 좋은 수이다.
좋은 수의 개수를 구하는 문제

- 투 포인터
'''

def answer_problem():
    N = int(input())
    nums = list(map(int, input().split(' ')))
    nums.sort()
    
    answer = 0
    
    for find in range(N):
        target = nums[find]
        p1, p2 = 0, N-1
        while p1 < p2:
            now = nums[p1] + nums[p2]

            if now == target:
                if p1 != find and p2 != find:
                    answer += 1
                    break
                else:
                    if p1 == find:
                        p1 += 1
                    elif p2 == find:
                        p2 -= 1
            elif now > target:
                p2 -= 1
            else:
                p1 += 1
        find+=1
    return answer

print(answer_problem())
