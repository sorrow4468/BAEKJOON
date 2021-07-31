a = int(input())
last_num = 1 # 출력값, 초기값은 1
sum_all = 0 # 1부터 전부 더한 값
while sum_all < a: # 전부 더한 값이 입력값보다 작을 때
    sum_all += last_num # 1부터 하나씩 더한다
    if sum_all >= a: # 전부 더한 값이 입력값보다 크거나 같으면
        break # while문 종료
    last_num += 1 # 그렇지 않으면 출력값을 계속 더하고
print(last_num) # 출력