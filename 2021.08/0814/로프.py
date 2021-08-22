"""
로프는 k개
k개의 로프로 w만큼을 나눠서 들어올릴 때
각 로프에 가해지는 하중은 w/k
로프의 최대하중이 w/k를 넘기면 안됌
모든 로프에 걸리는 하중은 w/k로 같고
제일 하중이 낮은 로프가 이를 버텨내야 한다
그 때의 w값
큰거부터 내려가야 한다
하중이 큰 로프부터 한개 두개 세개... 하다가 
최대하중이 계속 증가하는데 꺾이는 순간이 온다
"""

N = int(input()) # 줄의 개수
ropes = [] # 로프들 초기화
for n in range(N): # 로프 개수만큼 반복하면서
    ropes.append(int(input())) # 로프들 입력받기
ropes.sort() # 정렬하고
ropes.reverse() # 뒤집어서 중량이 큰 로프가 앞으로 오도록
max_weight = ropes[0] # 제일 중량이 큰 로프 혼자 있을때가 최대중량 초기값
for n in range(1, N+1): # 로프 1개부터 N개까지
    if max_weight <= ropes[n-1]*n: # 최대하중이 기존보다 크면
        max_weight = ropes[n-1]*n # 새로 저장
print(max_weight) # 최대하중 출력