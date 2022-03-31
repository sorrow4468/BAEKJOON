A, B = map(int, input().split())
chicken = int(input())
result = 0
if A+B >= chicken*2:
    result = A + B - chicken*2
else:
    result = A + B
print(result)