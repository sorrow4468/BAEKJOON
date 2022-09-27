import sys

input = sys.stdin.readline

UCPC = ('U', 'C', 'P', 'C')
sen = input().rstrip()
i, j = 0, 0 # sen, UCPC
for i in range(len(sen)):
    if j == 4: break
    if sen[i] == UCPC[j]: j += 1
print('I love UCPC' if j == 4 else 'I hate UCPC')