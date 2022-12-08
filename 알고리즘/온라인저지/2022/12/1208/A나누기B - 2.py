A, B = map(int, input().split())
print(f'{A//B}.', end='')
for _ in range(1001):
    A = (A%B)*10
    print(A//B, end='')