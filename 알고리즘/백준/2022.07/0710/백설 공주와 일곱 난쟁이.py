D = [int(input()) for _ in range(9)]
result = []
# print(D)
summ = sum(D)
for i in range(9):
    for j in range(i+1, 9):
        tmp = summ - (D[i]+D[j])
        if tmp == 100:
            result.append(D[i])
            result.append(D[j])
for d in D:
    if d not in result:
        print(d)