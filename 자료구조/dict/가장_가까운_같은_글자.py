# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    history = dict()
    
    # history에 가장 최근에 나온 위치를 저장하며 진행(이전 값은 필요 없음)
    for idx, alpha in enumerate(s):
        if alpha in history:
            answer.append(idx-history[alpha])
        else:
            answer.append(-1)
        history[alpha] = idx
    return answer