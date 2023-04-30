targets = [2**i for i in range(10)]
scores = [[0]*10 for _ in range(2)] # A, B
A, B = map(int, input().split())

for i in range(9, -1, -1):
    target = targets[i]

    if A>=target:
        scores[0][i] = 1
        A -= target

    if B>=target:
        scores[1][i] = 1
        B -= target

result = 0

for i in range(10):
    C, D = scores[0][i], scores[1][i]
    if (C == 0 and D == 1) or (C == 1 and D == 0):
        result += 2**i

print(result)