"""
O가 연속되는지 알 수 있는 법?
순회할 때
이번 값이 O인지 확인하고
몇번째 O인지 확인해서
인덱스만큼 더해주기
"""

T = int(input()) # 테스트 케이스 개수

for i in range(T): # 테스트 케이스 개수만큼 반복하면서
    O_and_X = input() # OX를 입력받고
    count = 0 # 연속된 O의 개수를 세는 count를 초기화 하고
    result = 0 # 결과값을 0으로 초기화하고
    for O_or_X in O_and_X: # OX를 순회하면서
        if O_or_X == "O": # 순회중인 값이 O면
            count += 1 # 연속된 O의 개수 +1
            result += count # O가 연속된 횟수값을 result에 저장
        else: # 순회중인 값이 X일때
            count = 0 # 연속된 O의 카운트를 초기화
    print(result) # 결과값 출력