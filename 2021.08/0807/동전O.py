"""
N = 동전의 종류 가짓수
K = 목표 금액
필요한 동전 개수의 최솟값을 구하는 문제
"""

N, K = map(int, input().split()) # 동전개수, 목표금액 입력
coins = [] # 입력받을 동전 리스트 초기화
for i in range(N): # 동전개수만큼 순회하면서
    coins.append(int(input())) # 동전들 입력받아서 추가
coins.reverse() # 입력받은 리스트 뒤집고
count = 0 # 필요한 동전개수 count 초기화
for coin in coins: # 동전들 순회하면서
    if coin <= K: # 이 동전이 목표금액보다 작으면
        while True: # 반복해서
            K -= coin # 목표금액에서 빼고
            count += 1 # 동전 개수 추가하고
            if coin > K: # 동전값이 목표금액보다 크면
                break # 정지
# 4200 -> 3200 -> 2200 -> 1200 -> 200 -> 100 -> 0
print(count) # 동전갯수 출력