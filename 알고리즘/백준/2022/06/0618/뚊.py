N, M = map(int, input().split())
char = []
is_same = []
for n in range(N):
    char.append(input())
for n in range(N):
    is_same.append(input())
result = 'Not Eyfa'
tmp = []
for i in range(N):
    tmp2 = ''
    for c in char[i]:
        tmp2 = tmp2 + c + c
    tmp.append(tmp2)
if tmp == is_same:
    result = 'Eyfa'
print(result)