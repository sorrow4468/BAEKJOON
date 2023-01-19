result = 0
for _ in range(int(input())):
    A, B = map(int, input().split())
    result += A*B
print(result)