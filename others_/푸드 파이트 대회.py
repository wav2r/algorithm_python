# 팰린드롬 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
answer = ''

    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    answer = answer + '0' + answer[::-1]
    return answer
