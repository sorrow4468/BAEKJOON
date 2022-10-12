def multiply(matrix1, matrix2): # 행렬 곱셈
    output = []
    for i in range(N):
        output.append([])
        for j in range(K):
            tmp = 0
            for k in range(M):
                tmp += matrix1[i][k] * matrix2[k][j]
            output[i].append(tmp)
    return output

N, M = map(int, input().split())
mat1 = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
mat2 = [list(map(int, input().split())) for _ in range(M)]
for i in multiply(mat1, mat2): print(*i)