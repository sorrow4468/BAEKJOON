from collections import deque

N = int(input())

if N == 1: # 입력값이 1이면 0을 곧바로 반환합니다
    print(0)
    exit()

# 1에서부터 거꾸로 탐색합니다
q = deque()
q.append((1, 0)) # 시작하는 1, 연산횟수 0부터 시작

check = set() # 중복연산 방지

while q:
    a = q.popleft()

    for i in [a[0]*3, a[0]*2, a[0]+1]: # 1에서 출발하기 때문에
        # 연산들을 거꾸로 실행
        if i == N: # N을 찾으면
            print(a[1]+1) # 연산횟수 1회 더하여 출력
            exit() # 바로 코드를 종료

        if i not in check and 1 <= i <= 1000000: # 가지치기
            # N은 1000000을 넘지 않는 자연수입니다
            check.add(i) # 범위를 만족하면 check에 추가
            q.append((i, a[1]+1)) # BFS 대기열에 추가
