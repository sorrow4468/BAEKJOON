N = int(input())
result = 0
if (not N%4 and N%100) or not N%400:
    result = 1
print(result)