N = int(input())
check = [tuple(map(int, input().split())) for _ in range(N)]
result = 0
for i in range(N-1):
    A, B = check[i], check[i+1]
    result += abs(A[0]-B[0]) + abs(A[1]-B[1])
dist = 0
for i in range(1, N-1):
    A, B, C = check[i-1], check[i], check[i+1]
    jump = abs(A[0]-C[0]) + abs(A[1]-C[1])
    no_jump = abs(A[0]-B[0]) + abs(A[1]-B[1]) + abs(B[0]-C[0]) + abs(B[1]-C[1])
    tmp = no_jump - jump
    dist = max(dist, tmp)
print(result - dist)

"""
구간을 점프할 때 얻을 수 있는 이익을 모아 테이블을 만든다
예제에서 B를 점프했을 때 얻는 이익값이 6
C를 점프했을 때 얻는 이익값이 4이다
그러면 B를 점프하는게 동선을 가장 단축시킬 수 있고
이 이익값 6을 전체 경로 20에서 빼주면 14가 나온다
0번과 N-1번을 제외한 점들에서
해당 점을 빼고 뛰었을 때 얻을 수 있는 이익값 테이블의
최대값을
전체 경로값에서 빼준다
"""