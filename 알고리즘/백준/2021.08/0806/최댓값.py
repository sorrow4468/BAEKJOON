"""
숫자를 다 받아서
리스트에 넣고
최댓값 찾아서
리스트 순회하면서
최댓값과 일치하는 요소의 인덱스(길이)
"""
numbers = [] # 입력받을 리스트 초기화
for i in range(9):
    numbers.append(int(input())) # Enter단위로 값들 입력받기
for i in range(len(numbers)): # 리스트를 순회
    if numbers[i] == max(numbers): # 최댓값과 순회중인 값이 같으면
        print(numbers[i]) # 값 출력
        print(i + 1) # 인덱스 출력
