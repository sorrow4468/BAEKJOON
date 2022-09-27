import sys

input = sys.stdin.readline

word = input().rstrip()
length = len(word)
change = []
for i in range(1, length-1):
    for j in range(i+1, length):
        A, B, C = word[:i][::-1], word[i:j][::-1], word[j:][::-1]
        change.append(A+B+C)
print(sorted(change)[0])