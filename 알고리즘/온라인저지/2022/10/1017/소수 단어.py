word = input()
num = 0
for w in word:
    if w.isupper(): # upper
        num += ord(w)-65+26+1
    else: # lower
        num += ord(w)-97+1
n = int(1e4)
a = [False, True] + [True]*(n-1)
for i in range(2, n+1):
    if a[i]:
        for j in range(2*i, n+1, i):
            a[j] = False
print('It is a prime word.' if a[num] else 'It is not a prime word.')