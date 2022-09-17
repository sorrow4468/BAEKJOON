from copy import deepcopy

N = int(input())
for k in range(1, 8): 
    if N == 3**k: break
width = k
square = ['*'*3] + ['* *'] + ['*'*3]

level = 0
tmp, result = deepcopy(square), deepcopy(square)

while level < k-1:
    level += 1
    result = []
    for s in tmp:
        result.append(s*3)
    for s in tmp:
        result.append(s + ' '*(3**level) + s)
    for s in tmp:
        result.append(s*3)
    tmp = deepcopy(result)
for r in result: print(r)

# https://www.acmicpc.net/problem/2447