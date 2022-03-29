A = list(map(int, input().split()))
B = list(map(int, input().split()))
point = [0, 0]
winner = ''
all_draw = True
for i in range(len(A)):
    if A[i] > B[i]:
        point[0] += 3
        all_draw = False
        if point[0] >= point[1]:
            winner = 'A'
    elif A[i] < B[i]:
        point[1] += 3
        all_draw = False
        if point[0] <= point[1]:
            winner = 'B'
    elif A[i] == B[i]:
        point[0] += 1
        point[1] += 1
if all_draw:
    winner = 'D'
print(*point)
print(winner)