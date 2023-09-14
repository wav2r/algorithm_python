'''
사용 알고리즘 : 투포인터

sum > N : start_index를 증가
sum < N : end_index를 증가
sum == N : 정답 (end_index를 증가시켜 다음 케이스를 탐색)

end_index가 N이 될때까지 이를 반복한다.

* 포인터를 옮기며 sum(now)의 값을 조정하여 일일히 계산하지 않는다.
'''

def answer_problem():
    N = int(input())
    
    start, end = 1, 1
    now = 1
    count = 0

    while end <= N:
        if now > N:
            now -= start
            start += 1
        elif now < N:
            end += 1
            now += end
        else: # sum == N
            count += 1
            end += 1
            now += end
    return count

print(answer_problem())
