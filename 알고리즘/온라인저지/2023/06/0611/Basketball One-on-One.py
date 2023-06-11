record = input()
A, B = 0, 0
for i in range(0, len(record), 2):
    player = record[i]
    if player == 'A':
        A += int(record[i+1])
    if player == 'B':
        B += int(record[i+1])
print('A' if A>B else 'B')