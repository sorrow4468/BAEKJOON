X = int(input())
for n in range(int(input())):
    A, B = map(int, input().split())
    X -= A*B
print('Yes' if X == 0 else 'No')