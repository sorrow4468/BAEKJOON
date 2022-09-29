import sys

input = sys.stdin.readline

word = list(input().rstrip())
i = 0
while i<len(word)-1:
    pikachu = word[i] + word[i+1]
    if pikachu in ['pi', 'ka']:
        for _ in [0]*2: word.pop(i); 
        continue
    if i<len(word)-2:
        pikachu = word[i] + word[i+1] + word[i+2]
        if pikachu == 'chu':
            for _ in [0]*3: word.pop(i); 
            continue
    i += 1
print('NO' if len(word) else 'YES')