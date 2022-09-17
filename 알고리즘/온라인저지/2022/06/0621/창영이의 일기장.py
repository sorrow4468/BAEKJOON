text = input()
result = ''
i = 0
while i < len(text):
    result = result + text[i]
    if text[i] in 'aeiou':
        i += 3
    else:
        i += 1
print(result)