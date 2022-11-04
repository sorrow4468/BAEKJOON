import sys

input = sys.stdin.readline

student = [
    'ABCABCABCABC',
    'BABCBABCBABC',
    'CCAABBCCAABB',
]
N = int(input().rstrip())
answer = input().rstrip()
result = [0, 0, 0]
for i in range(N):
    for j in range(3):
        if answer[i] == student[j][i%12]:
            result[j] += 1
IDs = ['Adrian', 'Bruno', 'Goran']
maxx = max(result)
print(maxx)
for i in range(3):
    if result[i] == maxx:
        print(IDs[i])