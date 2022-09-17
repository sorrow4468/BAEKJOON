N = int(input())
files = list(map(int, input().split()))
cluster = int(input())
result = 0
for file in files:
    if not file: continue
    if file > cluster:
        tmp = file//cluster + 1
        if file%cluster == 0: tmp -= 1
        result += cluster * tmp
    else:
        result += cluster
print(result)