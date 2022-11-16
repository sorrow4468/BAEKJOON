import sys

input = sys.stdin.readline

word = input().rstrip()
keyword = input().rstrip()
tmp = ''
for w in word:
    if w in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        tmp = tmp+w
print(1 if keyword in tmp else 0)