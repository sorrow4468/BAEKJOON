import sys

input = sys.stdin.readline

def lay_check(arr):
    cnt = 0
    for i in range(N):
        size = 0
        for j in range(N):
            if arr[i][j] == '.': size += 1
            else:
                if size>=2: cnt += 1   
                size = 0
        if size>=2: cnt += 1
    result.append(cnt)

N = int(input().rstrip())
arr = [input().rstrip() for _ in range(N)]
rotated_arr = []
result = []
lay_check(arr)
for j in range(N):
    tmp = ''
    for i in range(N):tmp += arr[i][j]
    rotated_arr.append(tmp)
lay_check(rotated_arr)
print(*result)

# https://www.acmicpc.net/problem/1652