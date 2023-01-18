for _ in range(int(input())):
    A, B = input().split()
    A = float(A)
    if B == 'kg':
        A *= 2.2046
        B = 'lb'
    elif B == 'lb':
        A *= 0.4536
        B = 'kg'
    elif B == 'l':
        A *= 0.2642
        B = 'g'
    else:
        A *= 3.7854
        B = 'l'
    print(f'{A:.4f} {B}')