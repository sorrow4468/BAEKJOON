import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    words = input().split()
    for word in words[2:]: print(word, end=' ')
    for word in words[:2]: print(word, end=' ')
    print()