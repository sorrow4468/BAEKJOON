A, B = map(int, input().split())
result = list(range(min(A, B)+1, max(A, B)))
print(len(result))
if result:
    print(*result)

# https://www.acmicpc.net/problem/10093