result = 0

text = input()

for t in text:
    if t in 'aeiou':
        result += 1

print(result)