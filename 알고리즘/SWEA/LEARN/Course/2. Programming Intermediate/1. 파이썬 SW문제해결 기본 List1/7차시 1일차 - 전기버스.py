T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split())) # 충전소 위치

    stop = [0] * (N+1) # 정류장 초기값

    for c in charge: # 충전소가 있는 정류장 정보를 갱신
        stop[c] = 1
        
    now = 0 # 현재 위치(초기 출발위치)
    cnt = 0 # 충전 횟수

    while now+K < N: # 목적지에 도달하기 전까지
        tmp = now # now값을 조작할 것이므로
        # 조작 전 now값을 tmp에 저장

        for i in range(now+K, now-1, -1): # 갈 수 있는 가장 멀리부터 
            # 현재 위치까지 거꾸로 확인하기
            if stop[i]: # 충전소가 발견되면
                # 뒤에서 탐색하였기 때문에
                # 가장 먼저 발견되는 충전소는 
                # 갈 수 있는 충전소 중 가장 멀리있는 충전소
                now = i # 해당 충전소의 위치로 이동
                cnt += 1 # 충전 한번 하였음
                break # 해당 for문 종료
        
        if i == tmp: # 충전소를 못찾고 결국 제자리로 돌아오면
            # 목적지에 도달할 수 없으므로
            cnt = 0 # 갈 수 없음
            break # while 종료

    print('#{} {}'.format(t, cnt))