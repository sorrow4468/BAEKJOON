a, d, k = map(int, input().split())
result = 1
if not (not (k-a)%d and (k-a)//d>=0): result = 'X'
else:
    result += (k-a)//d
print(result)