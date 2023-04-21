scores = []
for i in range(1, int(input())+1):
    scores.append(list(map(int, input().split()))+[i])
scores.sort(key=lambda x:(-x[0], x[1], x[2]))
print(scores[0][3])