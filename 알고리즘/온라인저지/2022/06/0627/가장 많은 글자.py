import sys
input = sys.stdin.read

S =  input().replace('\n', '').replace(' ', '')
A = [0] * 26
for s in S:
    A[ord(s)-97] += 1
result = ''
for i in range(26):
    if A[i] == max(A):
        result += chr(i+97)
print(result)