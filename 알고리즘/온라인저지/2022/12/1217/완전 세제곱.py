for a in range(1, 101):
    for b in range(2, a+1):
        for c in range(b, a+1):
            for d in range(c, a+1):
                tmp = b**3 + c**3 + d**3
                if a**3 == tmp:
                    print('Cube = {}, Triple = ({},{},{})'.format(a, b, c, d))