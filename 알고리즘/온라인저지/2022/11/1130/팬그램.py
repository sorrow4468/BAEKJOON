while True:
    S = input()
    if S == '*': break
    alphabet = [0]*26
    for s in S:
        if s == ' ': continue
        tmp = ord(s)-ord('a')
        if not alphabet[tmp]:
            alphabet[tmp] = 1
    print('Y' if sum(alphabet) == 26 else 'N')