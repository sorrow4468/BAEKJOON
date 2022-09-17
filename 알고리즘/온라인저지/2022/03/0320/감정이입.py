def dec_to_bin(X):
    m = 1
    output = 0
    for x in X[::-1]:
        if int(x):
            output += m
        m *= 2
    return output

A = input()
B = input()
print(bin(dec_to_bin(A)*dec_to_bin(B))[2:])