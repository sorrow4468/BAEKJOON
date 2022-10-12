N, C = map(int, input().split())
hanabi = [int(input()) for _ in range(N)]
result = 0
for i in range(1, C+1):
    fire = False
    for h in hanabi:
        if not i%h: fire = True
    result += int(fire)
print(result)