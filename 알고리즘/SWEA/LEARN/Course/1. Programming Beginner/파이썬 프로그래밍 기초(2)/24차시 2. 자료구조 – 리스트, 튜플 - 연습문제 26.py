l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]

result = []

for i in l1:
    for j in l2:
        if i == j:
            result.append(i)

print(result)