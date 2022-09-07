N, S = input(), input()
result = 0
for s in S:
    if s in 'aeiou': result += 1
print(result)