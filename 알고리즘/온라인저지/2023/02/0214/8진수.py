tmp = 0
i = 1
for j in input()[::-1]:
    tmp += i * int(j)
    i *= 2

import string

N, B = tmp, 8
tmp = string.digits + string.ascii_uppercase # 자릿수를 담은 문자열
result = ''
while N:
    result = tmp[N%B] + result # B진법이므로 B로 나눈 나머지번째 문자를 계속 추가한다
    N //= B
print(result)