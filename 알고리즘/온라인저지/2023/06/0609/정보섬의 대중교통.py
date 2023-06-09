N, A, B = map(int, input().split())
result = 'Anything'
if A>B: result = 'Subway'
if A<B: result = 'Bus'
print(result)