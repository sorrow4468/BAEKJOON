N = int(input())
M = int(input())
result = M
tunnel = M
zero = False
for n in range(N):
    A, B = map(int, input().split())
    tunnel += A
    tunnel -= B
    result = max(result, tunnel)
    if tunnel<0:
        zero = True
print(0 if zero else result)