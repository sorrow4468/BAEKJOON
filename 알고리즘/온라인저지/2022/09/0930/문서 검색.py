import sys

input = sys.stdin.readline

word = input().rstrip()
pattern = input().rstrip()
L = len(pattern)
i = 0
result = 0
while i<len(word)-L+1:
    if pattern == word[i:i+L]:
        result += 1
        i += L-1
    i += 1
print(result)