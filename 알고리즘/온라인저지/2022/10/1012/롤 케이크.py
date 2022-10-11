import sys

input = sys.stdin.readline

result = [[0, 0], [0, 0]]
L = int(input().rstrip())
N = int(input().rstrip())
cakes = [1]*L
for i in range(1, N+1):
    P, K = map(int, input().rstrip().split())
    if K-P+1 > result[1][1]:
        result[1][1] = K-P+1
        result[1][0] = i
    cake = 0
    for j in range(P-1, K):
        if cakes[j]:
            cakes[j] = 0
            cake += 1
    if cake > result[0][1]:
        result[0][1] = cake
        result[0][0] = i
print(result[1][0])
print(result[0][0])