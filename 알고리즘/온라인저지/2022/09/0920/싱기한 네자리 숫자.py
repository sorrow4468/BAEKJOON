import string

tmp = string.digits + string.ascii_uppercase # 자릿수를 담은 문자열
digits_dict = {
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15,
}

def change(num, base):
    result = ''
    while num:
        result = tmp[num%base] + result
        num //= base
    return result

def digits_sum(num, base):
    result = 0
    for n in num:
        result += digits_dict[n]
    return result

for num in range(1000, 10000):
    A, B, C = str(num), change(num, 12), change(num, 16)
    A, B, C = digits_sum(A, 10), digits_sum(B, 12), digits_sum(C, 16)
    if A == B == C: print(num)

# https://www.acmicpc.net/problem/6679