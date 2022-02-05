N = int(input())

answers = list(map(int, input().split()))

p = 0
result = 0

for a in answers:
    if a:
        p += 1
    else:
        p = 0
    
    result += p

print(result)