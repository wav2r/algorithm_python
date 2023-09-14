'''
사용 알고리즘 : 투포인터

left + right > target : right 감소
left + right < target : left 증가
left + right == target : 정답 (양쪽 포인트 모두 이동)

두 포인터가 만날 때까지 반복한다.
'''

def answer_problem():
    N = int(input())
    target = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    
    count = 0
    left, right = 0, N-1
    while left < right:
        now = arr[left] + arr[right]
        if now < target:
            left += 1
        elif now > target:
            right -= 1
        else: # now == target
            count += 1
            left += 1
            right -= 1
    return count

print(answer_problem())
