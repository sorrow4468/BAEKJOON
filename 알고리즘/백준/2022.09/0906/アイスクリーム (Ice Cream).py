S, A, B = int(input()), int(input()), int(input())
result = 250
while A < S:
    A += B
    result += 100
print(result)