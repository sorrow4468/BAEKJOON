S = input()
result = 0
if 'M' in S: result += 1
if 'O' in S: result += 1
if 'B' in S: result += 1
if 'I' in S: result += 1
if 'S' in S: result += 1
print('YES' if result == 5 else 'NO')