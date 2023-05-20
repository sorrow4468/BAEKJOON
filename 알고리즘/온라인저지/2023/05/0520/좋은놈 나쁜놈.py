for _ in range(int(input())):
    S = input()
    G = S.count('G')
    G += S.count('g')
    B = S.count('B')
    B += S.count('b')
    result = 'NEUTRAL'
    if G > B:
        result = 'GOOD'        
    if G < B:
        result = 'A BADDY'
    print(f'{S} is {result}')