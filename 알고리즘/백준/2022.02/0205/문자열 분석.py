upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'


while True:
    try:
        a = b = c = d = 0
        
        sen = input()
        
        for s in sen:
            if s in upper:
                b += 1
            elif s in lower:
                a += 1
            elif s in num:
                c += 1
            elif s == ' ':
                d += 1

        print(a, b, c, d)

    except:
        break