T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    result = []
	# 제곱까지 갈 필요없다 
    # A + B + C + D 가 가장 크면 결과값이 가장 클거다
    # 결과값만 (A+B)**2 + (C+D)**2 를 출력해주면 된다
    
    stack = []
    tmp = 0
    
    visited = [0] * N
    for i in range(N-6):
        stack.append(arr[i])
        visited[i-1], visited[i], visited[i+1] = 1, 1, 1
        for j in range(i, N-4):
            if visited[j] == 0:
                stack.append(arr[j])
                visited[j-1], visited[j], visited[j+1] = 1, 1, 1
                for k in range(j, N-2):
                    if visited[k] == 0:
                        stack.append(arr[k])
                        visited[k-1], visited[k], visited[k+1] = 1, 1, 1
                        for l in range(k, N):
                            if visited[l] == 0:
                                stack.append(arr[l])
                                if sum(stack) > tmp:
                                    tmp = sum(stack)
                                    result = [s for s in stack]
                                stack.pop()
                        visited[k-1], visited[k], visited[k+1] = 0, 0, 0
                        stack.pop()
                visited[j-1], visited[j], visited[j+1] = 0, 0, 0
                stack.pop()
        visited[i-1], visited[i], visited[i+1] = 0, 0, 0
        stack.pop()
    A = result[0]
    B = result[1]
    C = result[2]
    D = result[3]
    ans1 = (A+B)**2 + (C+D)**2
    ans2 = (A+D)**2 + (B+C)**2
    print('#{} {}'.format(t, (max(ans1, ans2))))

"""
input↓
5
10
80 90 65 55 90 60 40 35 30 25
8
30 25 70 55 95 75 90 20
10
60 85 45 25 15 70 55 70 85 35
15
80 30 35 95 45 85 30 25 100 85 10 60 80 30 5
20
45 30 5 85 55 85 10 5 75 60 15 65 45 50 75 80 15 10 50 90
"""