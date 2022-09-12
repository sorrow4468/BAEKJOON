"""
블록(구간)의 개수가 적은 숫자를 뒤집기
그냥 숫자의 개수가 적은 숫자를 뒤집기
"""
arr = list(map(int, list(input())))
# print(arr)
switch = True
result = [0, 0, arr.count(0), arr.count(1)]
switch = bool(arr[0])
result[switch] += 1
for a in arr:
    if a != switch:
        switch = not switch
        result[switch] += 1
# print(result)
print(min(result))