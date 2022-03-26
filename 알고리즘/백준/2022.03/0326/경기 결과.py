N = int(input())
result = [0, 0]
for n in range(N):
    A, B = map(int, input().split())
    if A > B:
        result[0] += 1
    elif B > A:
        result[1] += 1
print(*result)