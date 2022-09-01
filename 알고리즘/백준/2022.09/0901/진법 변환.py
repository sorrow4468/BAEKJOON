number = input().split()
N, B = number[0], int(number[1])
result = 0
N = N[::-1]
for i in range(len(N)):
    O = ord(N[i]) # ord
    if 48<=O<=57: O -= 48
    elif 65<=O<=90: O -= 55
    tmp = B**i*O
    result += tmp
print(result)