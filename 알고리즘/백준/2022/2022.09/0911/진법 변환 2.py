import string

N, B = map(int, input().split())
tmp = string.digits + string.ascii_uppercase # 자릿수를 담은 문자열
result = ''
while N:
    result = tmp[N%B] + result # B진법이므로 B로 나눈 나머지번째 문자를 계속 추가한다
    N //= B
print(result)