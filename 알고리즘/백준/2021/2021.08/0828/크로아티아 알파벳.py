import sys

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = sys.stdin.readline()
i = 0
cnt = 0
while i < len(word)-1:
    try:
        if word[i:i+2] in croatia:
            cnt += 1
            i += 2
        elif word[i:i+3] in croatia:
            cnt += 1
            i += 3
        else:
            cnt += 1
            i += 1
    except:
        pass
print(cnt)