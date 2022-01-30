sen = input()

LETTERS = 0
DIGITS = 0

for s in sen:
    if 65 <= ord(s) <= 90 or 97 <= ord(s) <= 122:
        LETTERS += 1

    if 48 <= ord(s) <= 57:
        DIGITS += 1

print('LETTERS', LETTERS)
print('DIGITS', DIGITS)
