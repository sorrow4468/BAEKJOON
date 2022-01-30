sen = input()

u = 0
l = 0

for s in sen:
    if 65 <= ord(s) <= 90:
        u += 1
    if 97 <= ord(s) <= 122:
        l += 1

print('UPPER CASE', u)
print('LOWER CASE', l)
