arr = [12, 24, 35, 70, 88, 120, 155]

result = []

for i in range(len(arr)):
    if i+1 in (1, 5, 6):
        continue
    result.append(arr[i])

print(result)