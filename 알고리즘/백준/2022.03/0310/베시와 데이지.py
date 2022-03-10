B = tuple(map(int, input().split()))
D = tuple(map(int, input().split()))
J = tuple(map(int, input().split()))

d = abs(D[0]-J[0]) + abs(D[1]-J[1])
b = max(abs(B[0]-J[0]), abs(B[1]-J[1]))

result = ''

if d < b:
    result = 'daisy'
elif b < d:
    result = 'bessie'
else:
    result = 'tie'

print(result)