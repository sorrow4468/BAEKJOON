import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    word = input().rstrip()
    prev, rear = word[:len(word)//2], word[len(word)//2:]
    rear = rear[::-1]
    print('Do-it' if prev[-1] == rear[-1] else 'Do-it-Not')