a, b = input().split() # a와 b를 공백을 기준으로 input 받아서
def aigosangsuya(a, b): 
    if int(a[::-1]) >= int(b[::-1]): # 각각 뒤에서 읽은 값의 int값을 비교해서
        result = a[::-1]
    else:
        result = b[::-1]
    return result # 큰 쪽을 저장해서 반환
print(aigosangsuya(a, b)) # 값을 출력