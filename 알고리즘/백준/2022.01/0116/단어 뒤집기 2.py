sen = input() # 입력

word = '' # 단어 혹은 태그

result = [] # 단어 혹은 태그 단위로 짤라서 담을 리스트

in_tag = False # 입력값을 돌면서, 현재 스캔중인 단어가 태그인지 확인

for s in sen: # 입력값을 하나씩 순회
    if s == '<': # 태그의 시작
        if word: # 단어가 추가되던 중이었으면
            result.append(word) # 추가중이던 단어를 끊어주고 리스트에 추가
            word = s # 태그를 담으면서 다시 시작
        else: # 시작 혹은 바로 앞에서 단어를 끊어줘서 단어가 없는 경우
            word = word + s # 태그를 담으면서 시작
        in_tag = True # 태그를 스캔중이므로 True
    elif s == '>': # 태그의 끝
        word = word + s # '>'를 담고
        result.append(word) # 리스트에 태그를 추가
        word = '' # 단어 초기화
        in_tag = False # 태그에 담는 것이 종료되었음
    elif s == ' ' and not in_tag: # 공백이면서 태그에 담는 중이 아닐 때
        result.append(word) # 태그가 아닌 그냥 단어를 리스트에 담고
        word = '' # 단어 초기화
    else: # 단어 혹은 태그를 스캔중
        word = word + s # 단어에 담아줌

if word: # 스캔이 끝난 마지막 단어
    result.append(word) # 리스트에 추가

# 첫번째 단어 출력
if result[0][0] == '<': # 태그이면
    print(result[0], end='') # 그대로 출력
else: # 단어이면
    print(result[0][::-1], end='') # 뒤집어서 출력
    
for i in range(1, len(result)): # 두번째 단어부터 끝까지 출력
    # 이전 단어가 태그가 아니고 지금 단어도 태그가 아니면
    if result[i-1][0] != '<' and result[i][0] != '<':
        print(end=' ') # 단어 사이 공백
    
    if result[i][0] == '<': # 지금 단어가 태그이면
        print(result[i], end='') # 그대로 출력
    else: # 단어이면
        print(result[i][::-1], end='') # 뒤집어서 출력