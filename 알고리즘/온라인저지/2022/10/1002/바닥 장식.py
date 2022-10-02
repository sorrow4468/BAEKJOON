import sys

input = sys.stdin.readline

def check(N, M, arr):
    board = 0
    for i in range(N):
        flag = False
        for j in range(M):
            if arr[i][j] == '-' and not flag:
                flag = True
                board += 1
            elif not arr[i][j] == '-': flag = False
    return board

def rotate(arr):
    rotated = []
    for j in range(M):
        tmp = ''
        for i in range(N): 
            if arr[i][j] == '-': tmp += '|'
            else: tmp += '-'
        rotated.append(tmp)
    return rotated

N, M = map(int, input().rstrip().split())
arr = [input().rstrip() for _ in range(N)]
result = 0
result += check(N, M, arr)
arr = rotate(arr)
result += check(M, N, arr)
print(result)