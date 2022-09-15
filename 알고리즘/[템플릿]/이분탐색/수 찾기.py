N = int(input())
arr1 = set(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
for a in arr2:
    if a in arr1: print(1)
    else: print(0)

# https://www.acmicpc.net/problem/1920