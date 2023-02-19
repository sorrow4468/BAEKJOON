def base_change(num, base):
    base_str = '0123456789abcdef'
    answer = 0
    power = 1

    for n in num[::-1]:
        answer += power*base_str.index(n)
        power *= base

    return answer

X = input()
result = 0

if X[0] == '0':
    if X[1] == 'x':
        result = base_change(X[2:], 16)
    else:
        result = base_change(X[1:], 8)
else:
    result = int(X)

print(result)