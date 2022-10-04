import sys

input = sys.stdin.readline

N, L = map(int, input().rstrip().split())
arr = sorted(list(map(int, input().rstrip().split())))
result = 0
while arr:
    tmp = arr[0]+L-1
    while arr and arr[0]<=tmp: arr.pop(0)
    result += 1
print(result)