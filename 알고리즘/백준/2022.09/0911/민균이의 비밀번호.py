N = int(input())
text_list = [input() for _ in range(N)]
text_set = set(text_list)
result = ''
for text in text_list:
    if result: break
    if text == text[::-1]:
        result = text
    elif text[::-1] in text_set:
        result = text
print(len(result), result[len(result)//2])