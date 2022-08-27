X = []
Y = []
for _ in range(2):
    tmp = list(map(int, input().split()))
    X.append(tmp[0])
    Y.append(tmp[1])
    X.append(tmp[2])
    Y.append(tmp[3])
print(max(max(X)-min(X), max(Y)-min(Y))**2)