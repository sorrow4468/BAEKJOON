import sys

input = sys.stdin.readline

def cut(length):
    cutted = 0
    for cable in cables:
        cutted += cable//length
    if cutted>=N: return True
    return False

K, N = map(int, input().rstrip().split())
cables = [int(input().rstrip()) for _ in range(K)]
result = 1
start, end = result, sum(cables)//N
while start<=end:
    mid = (start+end) // 2
    if cut(mid):
        start = mid+1
        result = max(result, mid)
    else:
        end = mid-1
print(result)

# https://www.acmicpc.net/problem/1654