def dfs(x, cnt):
    if cnt == 6: # 고른 숫자가 6개면
        for i in range(k): # 고른 숫자들을 전체 조회할 것
            if visited[i]: # 고른 숫자가 있으면
                print(tmp[i], end=' ') # 출력
        print() # 줄바꿈
        return # 해당 재귀 종료
    
    for i in range(x, k): # 숫자를 하나씩 선택할건데
        visited[i] = 1 # 해당 숫자 선택
        dfs(i+1, cnt+1) # 다음 숫자 선택하러
        visited[i] = 0 # DFS
        # 갔다가 찍고 되돌아오는 부분

while True:
    tmp = list(map(int, input().split()))
    
    if tmp[0] == 0:
        break

    k = tmp.pop(0)

    visited = [0] * k

    dfs(0, 0) # 0번째숫자부터, 고른숫자 0개부터

    print() # 매 케이스마다 줄바꿈