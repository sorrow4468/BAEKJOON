"""
8 4 2의 지름이 각각 같아야한다
파이를 생략하고
반지름 각각 A, B, C, ...
각각의 바퀴수는 A / B
이 바퀴수를 기약분수형태로 출력
A/B A/C ... 
테스트케이스 개수 T
"""

T = int(input()) # 테스트케이스 개수, 쓰지는 않았다
rs = list(map(int, input().split())) # 반지름 들 입력받아서 list()

def gcd(x, y): # 최대공약수 구하는 함수, 유클리드 호제법
    while y:
        x, y = y, x % y
    return x

for i in range(1, len(rs)): # 첫 링 제외하고 링의 반지름들 순회
    gcd_rs = gcd(rs[0], rs[i]) # 반지름들의 최대공약수 구해서
    print(f'{rs[0] // gcd_rs}/{rs[i] // gcd_rs}')
    # 각 링들을 기약분수 형태로 출력