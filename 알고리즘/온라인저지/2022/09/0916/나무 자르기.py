import sys

input = sys.stdin.readline

def cut(height):
    cutted = 0
    for tree in trees:
        if tree>height:
            cutted += tree-height
    if cutted>=M: return True
    return False

N, M = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))
result = 0
start, end = result, int(1e9)
while start<=end:
    mid = (start+end) // 2
    if cut(mid):
        start = mid+1
        result = max(result, mid)
    else: end = mid-1
print(result)

# https://www.acmicpc.net/problem/2805