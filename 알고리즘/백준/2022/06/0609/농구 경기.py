table = [0]*26
N = int(input())
for n in range(N):
    first = ord(input()[0]) - 97
    table[first] += 1
# print(table)
result = ''
for i in range(len(table)):
    if table[i] >= 5:
        result = result + chr(i+97)
if not result:
    result = 'PREDAJA'
print(result)