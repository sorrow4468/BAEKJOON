import sys

input = sys.stdin.readline

N, P = map(int, input().rstrip().split())
arr = [0]*(P+1)
flag = False
now = N
while not flag:
    now = (now*N)%P
    arr[now] += 1
    if arr[now] == 3: flag = True
print(arr.count(2) + 1)