pizza = 0
while True:
    tmp = input()
    if tmp == '0': break
    pizza += 1
    R, W, L = map(int, tmp.split())
    A = (R*2)**2
    B = W**2 + L**2
    result = 'fits'
    if A < B: result = 'does not fit'
    print(f'Pizza {pizza} {result} on the table.')