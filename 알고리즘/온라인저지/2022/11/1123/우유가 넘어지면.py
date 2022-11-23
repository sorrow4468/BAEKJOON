import sys

input = sys.stdin.readline

rotate = {
    ".": ".",
    "O": "O",
    "-": "|",
    "|": "-",
    "/": "\\",
    "\\": "/",
    "^": "<",
    "<": "v",
    "v": ">",
    ">": "^",
}

N, M = map(int, input().rstrip().split())
arr = [input().rstrip() for _ in range(N)]
for j in range(M-1, -1, -1):
    for i in range(N):
        print(rotate[arr[i][j]], end='')
    print()