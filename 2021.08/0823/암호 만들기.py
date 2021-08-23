L, C = map(int, input().split())
arr = list(input().split())

n = len(arr)
result = []
for i in range(1<<n):
    tmp = []
    for j in range(n):
        if i&(1<<j):
            tmp.append(arr[j])
    if len(tmp) == L:
        if ('a' in tmp) or ('e' in tmp) or ('i' in tmp) or ('o' in tmp) or ('u' in tmp):
            count = 0
            for tm in tmp:
                if tm in 'bcdfghjklmnpqrstvwxyz':
                    count += 1
            if count >= 2:
                tmp.sort()
                tmp2 = ''
                for t in tmp:
                    tmp2 = tmp2 + t
                result.append(tmp2)
result.sort()
for res in result:
    print(res)