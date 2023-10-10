#https://www.acmicpc.net/problem/1149
'''
동적계획법

오류 해결 => temp를 즉시 수정한 코드를 사용하여, 다음 연산에서 덮어쓰여진 temp가 사용되어 오류가 발생함
            plus에 더할 값을 저장해두고 temp에 반영하는 작업을 뒤로 미룸
'''

N = int(input())
temp = list(map(int, input().split(' ')))

for _ in range(N-1):
    rgb = list(map(int, input().split(' ')))
    plus = []
    plus.append(min(temp[1], temp[2]))
    plus.append(min(temp[0], temp[2]))
    plus.append(min(temp[0], temp[1]))

    for i in range(3):
        temp[i] = rgb[i] + plus[i]

print(min(temp))
