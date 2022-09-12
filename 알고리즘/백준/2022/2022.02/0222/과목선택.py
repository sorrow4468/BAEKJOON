science = [int(input()) for _ in range(4)]
social = [int(input()) for _ in range(2)]

science.sort(reverse=True)

result = 0

result += sum(science[:3]) + max(social)

print(result)