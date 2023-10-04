# 11399 : 삽입정렬 활용

N = int(input())

times = list(map(int, input().split()))

# 삽입 정렬
for i in range(1, N):
    j = 0
    while j < i and times[j] <= times[i]:
        j += 1
    find_index = j # insert index
    insert_value = times[i]
    for j in range(i, find_index, -1):
        times[j] = times[j-1]
    times[find_index] = insert_value

total_time = 0
for i in range(N):
    total_time += times[i] * (N-i)
print(total_time)
