N = int(input())
scores = list(map(int, input().split(' ')))
maxScore = max(scores)

answer = (sum(scores) / maxScore * 100) / N
print(float(answer))