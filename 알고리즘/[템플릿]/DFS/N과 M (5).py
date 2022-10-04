import sys

input = sys.stdin.readline

def solve(depth, N, M):
    if depth == M:
        print(*result); return
    for i in range(N):
        if not visited[i]:
            visited[i] = True; result.append(arr[i])
            solve(depth+1, N, M)
            result.pop(); visited[i] = False

N, M = map(int, input().rstrip().split())
arr = sorted(list(map(int, input().rstrip().split())))
visited = [False] * N
result = []
solve(0, N, M)

"""
BFS 돌 때 
방문하지 않았으면
방문처리, Q에 추가 해주듯이
DFS도 똑같이
함수 자체 메모리를 Q처럼 활용하면서
방문하지 않았으면
방문처리, 다음 탐색
나오면서 방문 풀어주고, 탐색점 취소해주고
그러니까
BFS DFS 차이는
다른건 다 같고, 방문지점을 당장갈거냐(DFS), 나중에 갈거냐(BFS) 인 것 같다
진짜 근데 DFS는 구현이 왤케 감이 안잡히냐 어렵네
"""

# https://www.acmicpc.net/problem/15654