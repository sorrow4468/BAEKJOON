import sys

input = sys.stdin.readline

def dfs(depth, start):
    if depth == M: 
        print(*result) 
        return
    for i in range(start, N):
        result.append(arr[i])
        dfs(depth+1, i)
        result.pop()

N, M = map(int, input().rstrip().split())
arr = sorted(list(map(int, input().rstrip().split())))
result = []
dfs(0, 0)

"""
<참고한 링크>
https://tmdrl5779.tistory.com/27
https://honggom.tistory.com/110
"""

# https://www.acmicpc.net/problem/15657