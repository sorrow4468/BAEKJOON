"""
미국동전
1: 페니 = 10원
5: 니켈 = 50원
10: 다임 = 100원
25: 쿼터 = 250

아래 두개는 문제에서 안 씀
# 50: 하프달러 = 500원
# 100: 달러 = 1000원
"""
T = int(input()) # 테스트케이스
coins = [25, 10, 5, 1] # 동전들
for t in range(T): # 테스트케이스 개수만큼
    change = int(input()) # 거스름돈
    changed_coins = [] # 사용된 모든 동전들
    for coin in coins: # 동전들을 순회하면서
        if coin <= change: # 거슬러줄 수 있으면
            while True: # while문 반복하면서 거슬러준다
                change -= coin # 해당 동전을 하나 거슬러주고
                changed_coins.append(coin) # 그 동전을
                    # 거슬러준 동전 리스트에 추가
                if coin > change: # 순회중인 동전이 금액보다 커져서
                    # 그 동전으로 거슬러 줄 수 없게되면
                    break # while문 종료
    for i in range(4): # 동전은 총 4개
        # 사용된 동전의 개수의 종류는 4개
        print(changed_coins.count(coins[i]), end=' ')
            # 동전개수를 세서 출력
    print() # 줄바꿈
    