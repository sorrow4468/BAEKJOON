for _ in range(int(input())):
    arr = [0]*26
    for s in input():
        char = s.lower()
        if 97 <= ord(char) < 97+26:
            arr[ord(char)-97] = 1
    result = 'missing '
    for i in range(26):
        if not arr[i]:
            result = result + chr(i+97)
        if i == 25 and result != 'missing ': break
    else: result = 'pangram'
    print(result)