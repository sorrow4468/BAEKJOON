L, R = map(int, input().split())
result = 'Not a moose'
if L == R:
    if L:
        result = f'Even {L*2}'
else:
    result = f'Odd {max((L,R))*2}'
print(result)
