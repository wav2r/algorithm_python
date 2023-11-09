#기수 정렬 문제
#기수 정렬의 알고리즘을 그대로 구현한 코드 : 메모리 초과
def now(num, d):
    return num % d // (d//10)

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

max_value = max(numbers) * 10 + 1
div = 10

while max_value > div:
    temp = [list() for _ in range(10)]

    for number in numbers:
        temp[now(number, div)].append(number)
    
    numbers = []

    # merge temp
    for arr in temp:
        numbers += arr
    div = div * 10

print(numbers)