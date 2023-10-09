# 11004 : 퀵 정렬
# 시간 초과 에러
import sys
sys.setrecursionlimit(10**6)

N, K = list(map(int, input().split()))
nums = list(map(int, input().split()))

def swap(a, b, arr):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp
    return arr

# insert pivot value(loc:0) to index
def insert_pivot(insert_index, arr):
    pivot_value = arr[0]

    for i in range(insert_index):
        arr[i] = arr[i+1]
    arr[insert_index] = pivot_value
    return arr

def qsort(arr):
    if len(arr) <= 1:
        return arr

    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr = swap(0, 1, arr)
        return arr

    pivot_index = len(arr)//2
    pivot = arr[pivot_index]
    arr = swap(0, pivot_index, arr)
    left, right = 1, len(arr)-1
    ''' 
    조건
    left의 값이 pivot보다 작은 경우 left++
    right의 값이 pivot보다 큰 경우 right--
    위의 두가지 조건을 동시에 만족하는 경우 swap하고 left++, right--
    '''
    while left < right:
        while pivot < arr[right] and right > 0:
            right -= 1
        while pivot > arr[left] and left < len(arr) - 1:
            left += 1

        if left <= right:
            arr = swap(left, right, arr)
            left += 1
            right -= 1
    
    # pivot의 값에 따라 왼쪽 혹은 오른쪽에 pivot 데이터를 삽입
    left = (left+right)//2
    insertIndex = left if arr[left] < pivot else left - 1

    arr = insert_pivot(insertIndex, arr)
    left_arr = qsort(arr[:insertIndex])
    mid_arr = [pivot]
    right_arr = qsort(arr[insertIndex+1:]) 
    return left_arr + mid_arr + right_arr

nums = qsort(nums)
print(nums[K-1])
