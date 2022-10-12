for i in range(int(input().rstrip())):
    word = input().lower()
    print('Yes' if word == word[::-1] else 'No')