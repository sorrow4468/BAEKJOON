N, M = map(int, input().split())
castle = [list(input()) for _ in range(N)]
row = set()
col = set()
for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row.add(i)
            col.add(j)
print(max(N-len(row), M-len(col)))