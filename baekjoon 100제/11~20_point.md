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

## 정렬

> 정렬의 종류와 작동 방식을 익히기 위한 알고리즘 작성으로, 효율적인 방법인 것은 아님

### 15 버블 정렬: 수 정렬하기1

- **버블 정렬**: 인접한 두 데이터의 크기를 비교해서 정렬하는 방법
- 시간복잡도: $O(n^2)$

### 16 버블 정렬 프로그램

오른쪽으로 이동하며 2개의 값을 비교하고 swap하는 과정에서 오른쪽에서 왼쪽으로 이동하는 범위는 한 loop에 한 칸이다.
이를 이용하여 오른쪽에서 왼쪽으로 이동하는 최대값을 구한다

`maxValue <  value[1] - idx` 에서 '절댓값'을 붙였을 때 오답이 나오는 이유

> 왼쪽에서 오른쪽으로 이동하는 경우는, swap의 이동 방향과 같으므로 한칸씩 이동하지 않는다. 그래서 오른쪽에서 왼쪽으로 이동하는 경우만 고려해야 한다.

### 17 선택 정렬: 내림차순으로 자릿수 정렬하기

- **선택 정렬**: 최솟값 혹은 최댓값을 찾아 남은 정렬 부분의 가장 앞에 있는 데이터와 swap한다
- 시간복잡도: $O(n^2)$

### 18 삽입 정렬: ATM 인출 시간 계산하기

- **삽입 정렬**: 정렬된 데이터 범위에서 정렬되지 않은 데이터의 적절한 위치를 찾아 삽입하는 정렬 방식
- 시간복잡도: $O(N^2)$

- 어려웠던 부분 >> 데이터를 삽입하려는 지점(insert index)에 데이터를 삽입하고 원래 있던 데이터를 뒤로 이동시키는 부분

```
find_index = j # insert index
    insert_value = times[i]
    for j in range(i, find_index, -1):
        times[j] = times[j-1]
    times[find_index] = insert_value
```

- 위처럼 구현한다
- 1 2 4 5 3 에서 3을 index=2 지점에 삽입하는 경우를 생각하면 3이라는 값을 별도로 저장해두고 역순으로 돌며 데이터를 한칸씩 뒤로 미룬다

### 19 퀵 정렬: K번째 수 구하기

> 퀵 정렬을 익히기 위해 사용한 것으로 비효율적인 알고리즘
> `sort`를 사용한 방법과 비교했을 때 비슷한 시간복잡도, 공간복잡도를 보였다.

```
import sys
sys.setrecursionlimit(10**7)
```

- recursion limit error 방지

```
def quickSort(start, end, K):
    global arr

    if start < end:
        pivot = partition(start, end)
        if pivot == K:
            return
        elif K < pivot:
            quickSort(start, pivot - 1, K)
        else:
            quickSort(pivot + 1, end, K)
```

- pivot(인덱스 값)의 위치에는 위치가 확정된 값이 들어간다(좌: pivot보다 작은 값/ 우: pivot보다 큰 값)
- 그러므로 만약 pivot과 K가 동일하다면 더이상 정렬할 필요가 없으므로 탐색을 종료한다
- 그렇지 않은 경우,
- K < pivot이라면 좌측에서 다시 퀵정렬을 실행
- 아니라면 우측에서 다시 퀵정렬을 실행

```
# 입력: start, end (퀵 정렬을 하려는 범위)
# 출력: 현재 pivot의 위치(배열 내에서의 위치가 확정된 곳)
def partition(start, end):

    global arr

    if start + 1 == end:
        if arr[start] > arr[end]:
            swap(start, end)
        return end

    mid = (start + end) // 2
    swap(start, mid)
    pivot = arr[start]

    i = start + 1
    j = end

    while i <= j:
        while pivot < arr[j] and j > 0:
            j = j - 1
        while pivot > arr[i] and i < len(arr) - 1:
            i = i + 1
        if i <= j:
            swap(i, j)
            i = i + 1
            j = j - 1

    arr[start] = arr[j]
    arr[j] = pivot
    return j

quickSort(0, N - 1, K - 1)
print(arr[K - 1])
```

- 왼쪽 포인터(i), 오른쪽 포인터(j) 두개를 이용한다
- pivot의 왼쪽에는 pivot보다 작은 값, pivot의 오른쪽에는 pivot보다 큰 값을 두어야 한다는 것을 생각함 =>
- pivot보다 큰 값을 발견할 때까지 왼쪽 포인터를 움직인다
- pivot보다 작은 값을 발견할 때까지 오른쪽 포인터를 움직인다
- i, j 위치의 값을 swap

- 마지막에 pivot(0으로 보내둔 값)과 swap할 값은 pivot보다 작은 값이어야 한다
- 그러므로 j를 선택
  - 만약 i, j가 swap된 경우라도 j가 큰 값을 찾아내고 swap되었기 때문에 작은 값이 있다
  - swap되지 않은 경우라도 swap되지 않았다면 큰 값을 찾아내지 못하고 작은 값을 가리키고 있을 것이다

### 20 병합 정렬: 수 정렬하기2

- 첫 시도에서 시간 초과가 나왔다.
- 배열들을 실제로 생성하여 더하는 module들을 작성하여 사용했는데 이로 인해 시간이 많이 걸린 것 같다.
- 책에 실려있는 배열은 그대로 두고 포인터를 이동하는 방식으로 재도전
