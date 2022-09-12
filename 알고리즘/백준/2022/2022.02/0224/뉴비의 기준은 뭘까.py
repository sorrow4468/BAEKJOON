N, M = map(int, input().split())

result = 'NEWBIE!'

if M <= N and M > 2:
    result = 'OLDBIE!'
elif M > N:
    result = 'TLE!'

print(result)