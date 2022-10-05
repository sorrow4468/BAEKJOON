import sys

input = sys.stdin.readline
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def idx(char):
    return ord(char)-65

def dfs(y, x, move):
    global result
    result = max(result, move)
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<R and 0<=nx<C and not visited[idx(arr[ny][nx])]:
            visited[idx(arr[ny][nx])] = 1
            dfs(ny, nx, move+1)
            visited[idx(arr[ny][nx])] = 0

R, C = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in ' '*R]
visited = [0]*26
result = 0
visited[idx(arr[0][0])] = 1
dfs(0, 0, 0)
print(result+1)

"""
처음으로 스스로 풀은 DFS문제인 것 같다
채점속도가 좀 느려서, 이게 정답이 될 까 걱정이 되었는데
신기하게도 정답이었다
BFS에서 다음 탐색점을 Q에 넣듯이
DFS에서 다음 탐색점을 재귀로 함수를 실행해주는 코드를 짰다
"""

# https://www.acmicpc.net/problem/1987