S = input() # 단어를 입력받아서
result = [-1] * 26 # 결과값을 -1 26개로 초기화해주고 
for s in S: # 알파벳을 순회하면서 
    for i in range(len(result)): # 그리고 result를 순회하면서
        if s == chr(97+i): # 단어의 해당 알파벳을 확인해서
            result[i] = S.index(s) # 알파벳의 index값의 등장위치를
                # result에 추가하고
for res in result: # result를 순회하면서
    print(res, end=' ') # 출력