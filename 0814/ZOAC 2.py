"""
시계모양에서 알파벳간에 거리는 ASCII 코드로 |A-B|
13을 초과하면 26-|A-B|
"""
word = input()                              # 입력받을 단어
word = 'A' + word                           # 단어의 맨 앞에 시작점인 A 추가
def zoac(A, B):                             # 글자간 거리를 구하는 함수 zoac()
    if abs(ord(A)-ord(B)) > 13:             # 두 글자의 거리가 13을 초과하면
        result = 26 - abs(ord(A)-ord(B))    # 26에서 거리만큼을 빼줌
                                            # 한바퀴(26)에서 거리만큼 뒤로 오겠다는 뜻
    else:                                   # 거리가 13아래면
        result = abs(ord(A)-ord(B))         # 거리 = 절대값
    return result                           # 결과 반환
sum_word = 0                                # 글자간 거리를 더할 변수
for i in range(1, len(word)):               # 2번째 글자부터 마지막 글자까지
                                            # 두 글자씩 비교할 것이기 때문
    sum_word += zoac(word[i-1], word[i])    # 글자간 거리들을 변수에 더하고
print(sum_word)                             # 거리들을 더한 값을 출력