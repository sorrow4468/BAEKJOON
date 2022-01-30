T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(T):
    N, M, L = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]

    start = ''
    goal = ''
    for i in range(N):
        if 2 in arr[i]:
            start = (arr[i].index(2), i)
        
        if 3 in arr[i]:
            goal = (arr[i].index(3), i)
        
    print(start, goal)


