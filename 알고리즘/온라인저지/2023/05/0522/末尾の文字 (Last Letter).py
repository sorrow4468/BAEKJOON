input()
S = input()
if S[-1] == 'G':
    S = S[:len(S)-1]
else:
    S += 'G'
print(S)