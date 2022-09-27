import sys

input = sys.stdin.readline

scores = []
for i in range(1, 9): scores.append([int(input().rstrip()), i])
scores.sort(key=lambda x:-x[0])
result = [0]
for score in scores[:5]:
    result[0] += score[0]
    result.append(score[1])
print(result[0])
print(*sorted(result[1:]))