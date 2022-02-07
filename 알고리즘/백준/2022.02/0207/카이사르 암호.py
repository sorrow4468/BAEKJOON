word = input()

for w in word:
    if ord(w)-3 < ord('A'):
        print(chr(ord(w)-3+26), end='')
    else:
        print(chr(ord(w)-3), end='')