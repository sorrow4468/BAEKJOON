a = int(input()) # a를 정수로 입력받고
b = input() # b를 str 그대로 입력받아서
c = 1 * int(b) # c에 b를 백업해두고
b = list(b) # b는 리스트로 ['3', '8', '5']로 만들어 준 다음
calc_list = [] # 각각의 계산값들을 더해서 리스트에 [0], [1], [2]에 저장할 리스트를 만들어주고
for i in range(3): # 리스트를 순회하면서 
    calc_list.append(a * int(b[i])) # 각각 자릿수를 곱한 값들을 구해서 저장
calc_list.reverse() # 결과값들을 뒤집어서
for calc in calc_list: # 결과값 리스트를 순회하면서
    print(calc) # 출력
print(a * c) # 마지막에 백업해놓은 원래b값과 a값을 곱해서 출력