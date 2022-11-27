import sys

input = sys.stdin.readline

result = [0, 0] # JOI, IOI
S = input().rstrip()
for i in range(len(S)-2):
    if S[i:i+3] == 'JOI': result[0] += 1
    elif S[i:i+3] == 'IOI': result[1] += 1
for r in result: print(r)