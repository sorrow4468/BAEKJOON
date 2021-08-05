a = int(input())

def calc(a): # 제시된 계산 규칙을 함수로 정의하고
    result = ((a % 10) + (a // 10)) % 10 + (a % 10) * 10
    return result

calc_list = [a] # 계산된 수들을 저장할 리스트의 0번째를 a로 초기화
i = 0 # while문 돌리기 위한 i
while True:
    calc_list.append(calc(calc_list[i])) # 함수를 적용하여 리스트에 추가
    i += 1
    if calc_list[0] == calc_list[::-1][0]: # 첫항(입력값)과 계산해서 추가한 값이 같을 때
        break # while문 종료하고
print(len(calc_list)-1) # 사이클 수 구해서 출력