alphabet = {}

tmp = input()

for t in tmp:
    if t not in alphabet:
        alphabet.update({t:1})
    else:
        alphabet[t] += 1

for a in alphabet:
    print('{},{}'.format(a, alphabet[a]))