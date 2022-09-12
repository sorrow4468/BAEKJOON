N = int(input())
prev, next, line, move = 0, 0, 0, 0
D = 1 # 우상향: 1, 좌하향: 0
for cnt in range(1, int(1e9)):
    next += cnt
    if prev <= N <= next:
        line, move = cnt, N-prev-1
        D = line%2
        break
    prev += cnt
# print(line, move, D)
A, B = 1, line
for i in range(move):
    A += 1
    B -= 1
if D: A, B = B, A
print(f'{A}/{B}')