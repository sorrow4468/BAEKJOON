sen = input()

for s in sen:
    o = ord(s)
    if s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if o <= ord('M'):
            print(chr(o + 13), end='')
        else:
            print(chr(o - 13), end='')
    elif s in 'abcdefghijklmnopqrstuvwxyz':
        if o >= ord('n'):
            print(chr(o - 13), end='')
        else:
            print(chr(o + 13), end='')
    else:
        print(s, end='')

