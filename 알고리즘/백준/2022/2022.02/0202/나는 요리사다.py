winner = 0
max_p = 0

for i in range(1, 6):
    p = sum(list(map(int, input().split())))
    if p > max_p:
        max_p = p
        winner = i

print(winner, max_p)