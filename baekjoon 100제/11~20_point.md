## Stack

### 11 스택으로 수열 만들기

- 후입선출인 스택의 원리를 이용하는 문제

```
import sys
input = sys.stdin.readline
```

시간복잡도 개선에 중요함!!

### 12 오큰수

- 스택을 이용
- 새로 들어오는 수가 top에 존재하는 수보다 크면 그 수는 오큰수가 된다
- stack에 a(0), b(1)가 존재할 경우 a의 오큰수를 발견할 경우 무조건 b의 오큰수가 된다.

### 13 카드 게임

- queue의 선입선출을 이용

### 14 절댓값 힙 구현하기

- PriorityQueue
- 우선순위 큐 이용

> 우선순위 큐의 연산
> `from collections import deque` : import
> `queue.put((abs(x), x))`: 첫번째 원소 기준으로 정렬됨
> `queue.get()[1]` : 두번째 원소 값을 사용함(첫번째는 우선순위용)

> 시간복잡도 줄이기<br>

```
import sys

input = sys.stdin.readline
print = sys.stdout.write
```
