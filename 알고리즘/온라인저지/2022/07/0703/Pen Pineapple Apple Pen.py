N = int(input())
word = input()
result = 0
idxs = []
for i in range(N-3):
    tmp = word[i:i+4]
    if tmp == 'pPAp':
        is_used = False
        for j in range(i, i+4):
            if j in idxs:
                is_used = True
        if not is_used:
            result += 1
            idxs += list(range(i, i+4))
print(result)