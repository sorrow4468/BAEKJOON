O = False # combo over
N = int(input())
result = 0
S = [[], []] # stack
for i in list(input()):
    if O: break
    try: # 1~9
        i = int(i)
        result += 1
    except: # LRSK
        if i == 'L': S[0].append(i)
        elif i == 'S': S[1].append(i)
        elif i == 'R':
            if S[0]:
                S[0].pop()
                result += 1
            else:
                O = True
        elif i == 'K':
            if S[1]:
                S[1].pop()
                result += 1
            else:
                O = True
print(result)