M = int(input())
D = int(input())

result = ''

if M == 2 and D == 18:
    result = 'Special'
elif M < 2:
    result = 'Before'
elif M > 2:
    result = 'After'
elif M == 2:
    if D < 18:
        result = 'Before'
    elif D > 18:
        result = 'After'

print(result)