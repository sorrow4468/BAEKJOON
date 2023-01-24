import string

def base_change(number, base):
    tmp = string.digits + string.ascii_uppercase + string.ascii_lowercase + '!@#$%^' # 자릿수를 담은 문자열
    result = ''
    while number:
        result = tmp[number%base] + result # B진법이므로 B로 나눈 나머지번째 문자를 계속 추가한다
        number //= base
    return result

for _ in range(int(input())):
    T = int(input())
    result = 0
    for base in range(2, 65):
        new_num = base_change(T, base)
        if new_num == new_num[::-1]:
            result = 1
            break
    print(result)