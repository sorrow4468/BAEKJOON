A, B, C = map(int, input().split())
N = int(input())
result = []
for n in range(N):
    tmp = 0
    for i in range(3):
        a, b, c = map(int, input().split())
        tmp += a*A + b*B + c*C
    result.append(tmp)
print(max(result))