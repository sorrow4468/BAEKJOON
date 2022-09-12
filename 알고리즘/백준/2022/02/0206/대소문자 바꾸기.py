sen = input()

for s in sen:
    if s.isupper():
        print(s.lower(), end='')
    elif s.islower():
        print(s.upper(), end='')
    else:
        print(s, end='')