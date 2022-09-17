M = int(input())
moves = []
for m in range(M):
    moves.append(tuple(map(int, input().split())))
# print(moves)
ball = 1
for move in moves:
    if ball in move:
        for m in move:
            if ball != m:
                ball = m
                break
print(ball)