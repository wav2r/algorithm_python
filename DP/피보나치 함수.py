# 피보나치 함수
# https://www.acmicpc.net/problem/1003

'''
IndexError
cache = [0 for _ in range(max(number))] < max같은 변동적인 값이 아닌 조건에 따라최댓값인 41로 수정하여 해결
'''
def fibonacci(n):
    if cache[n]:
        return cache[n]
    else:
        temp1 = fibonacci(n-1)
        temp2 = fibonacci(n-2)
        cache[n] = [temp1[0] + temp2[0], temp1[1] + temp2[1]]
        return cache[n]

T = int(input())
number = []
for _ in range(T):
    number.append(int(input()))
    
cache = [0 for _ in range(41)]
cache[0] = [1, 0]
cache[1] = [0, 1]

for i in range(T):
    print(*fibonacci(number[i]))