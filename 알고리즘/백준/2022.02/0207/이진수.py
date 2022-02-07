T = int(input())

for t in range(T):
    N = int(input())

    binary = (str(bin(N))[::-1])[:-2]

    for i in range(len(binary)):
        if binary[i] == '1':
            print(i, end=' ')