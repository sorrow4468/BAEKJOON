numbers = [] # 입력받을 숫자의 리스트 초기화
for i in range(3): # A, B, C 세개의 숫자를 입력받음
    numbers += [int(input())] # 입력받아서 리스트에 추가
multipled = 1 # 다 곱한 값의 초기값 1:O, 0:X
for number in numbers: # multipled에 입력받은 숫자 곱해서 집어넣었고
    multipled *= number
multipled = str(multipled) # 곱한 값을 str로 변경
counts = [] # 숫자들을 셀 리스트 초기화
for i in range(10):
    counts.append([]) # 각 카운트들을 담을 빈 리스트 생성
for num in multipled:
    for i in range(10):
        if num == str(i): # 순회중인 숫자가 0~9중에 일치하는 수를
            counts[i] += [1] # 확인해서 count 한 번
for i in range(10):
    counts[i] = sum(counts[i]) # 카운트한 숫자는 [1, 1, 1] 이렇게 되 있으니까
        # 다 더한 값을 카운트에 재설정
for count in counts:
    print(count) # 카운트값들을 출력