all = set()

for i in range(1, 10):
    for j in range(1, 10):
        all.add(i * j)

all.discard(1)

for i in range(3, 82, 3):
    for j in range(7, 82, 7):
        if i in all:
            all.discard(i)
        elif j in all:
            all.discard(j)

result = [[] for _ in range(8)]

for i in range(2, 10):
    tmp = 0
    for j in range(i, 82, i):
        tmp += 1
        if j in all:
            result[i-2].append(j)
        if tmp == 9:
            break

print(result)