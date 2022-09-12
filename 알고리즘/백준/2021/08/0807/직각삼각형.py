"""
입력받는 변 3개 A, B, C
0 0 0 입력받으면 실행 종료
피타고라스 정리 <if a**2 + b**2 == c**2: 직각삼각형>
"""

while True: # 계속 반복하는 while True
    A, B, C = map(int, input().split()) # 각 변을 입력받고
    if A + B + C == 0: # 마지막 줄인 0 0 0 이면
        break # 종료
    if A**2 + B**2 + C**2 == ((max(A, B, C))**2) * 2: # 직각삼각형이면
        # 가장 큰 수만 찾아서 구하는 공식을 위와같이 구성하였음
        print('right') # 출력
    else: # 직각삼각형 아니면 
        print('wrong') # 출력
