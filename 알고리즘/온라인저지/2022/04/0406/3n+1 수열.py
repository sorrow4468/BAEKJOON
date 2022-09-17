N = int(input())
result = 0
while True:
    if N == 1:
        break
    if N % 2:
        N = N*3 + 1
    else:
        N //= 2
    result += 1
print(result+1)