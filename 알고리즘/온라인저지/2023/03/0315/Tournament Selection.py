result = -1
cnt = 0
for _ in range(6):
    if input() == 'W':
        cnt += 1
if cnt == 1 or cnt == 2:
    result = 3
if cnt == 3 or cnt == 4:
    result = 2
if cnt == 5 or cnt == 6:
    result = 1
print(result)