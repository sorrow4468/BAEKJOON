import sys

N, M = map(int, sys.stdin.readline().split())

arr = tuple(map(int, sys.stdin.readline().split()))

tmp = [arr[0]]

for n in range(1, N):
    tmp.append(arr[n]+tmp[-1])

for m in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        print(tmp[b-1])
    else:
        print(tmp[b-1]-tmp[a-2])
