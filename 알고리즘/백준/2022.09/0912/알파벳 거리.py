for _ in range(int(input())):
    X, Y = input().split()
    result = []
    for i in range(len(X)):
        y, x = ord(Y[i])-64, ord(X[i])-64
        tmp = y-x
        if tmp < 0: tmp += 26
        result.append(tmp)
    print('Distances:', *result)