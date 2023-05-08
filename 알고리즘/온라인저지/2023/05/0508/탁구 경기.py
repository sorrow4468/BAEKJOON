D, P = 0, 0
for i in range(int(input())):
    winner = input()
    if abs(D-P) == 2:
        continue
    if winner == 'D':
        D += 1
    if winner == 'P':
        P += 1
print(f'{D}:{P}')