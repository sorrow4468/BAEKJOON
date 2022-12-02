for _ in range(int(input())):
    S = input()
    if S[1] == '=':
        print('skipped')
    else:
        result = map(int, S.split('+'))
        print(sum(result))