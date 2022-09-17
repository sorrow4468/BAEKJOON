while True:
    sen = input()
    if sen == '#':
        break
    result = 0
    for s in sen:
        if s in 'aeiouAEIOU':
            result += 1
    print(result)