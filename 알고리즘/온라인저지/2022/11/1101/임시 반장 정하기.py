import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
check = [set() for _ in range(N)]
for j in range(5):
    for i in range(N):
        for k in range(N):
            if arr[i][j] == arr[k][j] and i != k:
                check[i].add(k)
result = [len(c) for c in check]
print(result.index(max(result))+1)