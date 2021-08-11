"""
1000엔에서 물건값 빼고
거스름돈을 거슬러주면 된다
동전의 최소개수"""
price = int(input()) # 물건의 가격
change = 1000-price # 거스름돈
coins = [500, 100, 50, 10, 5, 1] # 동전들
count = 0 # 동전의 개수 초기화
for coin in coins: # 동전들을 금액이 큰 순서로 순회하면서
    if coin <= change: # 거슬러줄 수 있으면
        while True:
            change -= coin # 해당 동전을 하나 거슬러주고
            count += 1 # 동전 개수 증가
            if coin > change: # 거슬러주지 못하면
                break # 종료하고 다음 작은 동전으로
print(count) # 동전 개수 출력