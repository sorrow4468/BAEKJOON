word = input()
word = word.upper()
alphabet = [0] * 26
for wrd in word:
    alphabet[ord(wrd)-65] += 1
if alphabet.count(max(alphabet)) > 1:
    print('?')
else:
    print(chr(alphabet.index(max(alphabet))+65))
