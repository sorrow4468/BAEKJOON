N, K = map(int, input().split())
q = list(range(1, N+1))
pointer = K-1
result = []
while q:
    result.append(q.pop(pointer))
    pointer += K - 1
    if not len(q):
        break
    else:
        pointer %= len(q)
    
print('<', end='')
print(result[0], end='')
for i in range(1, len(result)):
    print(',', result[i], end='')
print('>')