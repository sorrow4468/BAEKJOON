result = 0
while True:
    try:
        input()
        result += 1
    except EOFError:
        break
print(result)