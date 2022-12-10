A, B = map(str, sorted(list(map(int, input().split()))))
result = ''
for i in range(1, len(B)+1):
    try:
        result = str(int(A[-i]) + int(B[-i])) + result
    except:
        result = str(int(B[-i])) + result
print(result)