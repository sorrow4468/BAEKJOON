from math import factorial as fact

N = int(input())
result = 0
if N == 3:
    result = 0
else:
    result = fact(N)
    result //= 24
    result //= fact(N-4)
print(result)