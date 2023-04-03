K = int(input())
for tc in range(1, K+1):
    H = int(input())
    action = input()
    for a in action:
        if H:
            if a == 'c': H += 1
            elif a == 'b': H -= 1
        else: break
    print(f'Data Set {tc}:')
    print(H)
    if tc != K: print()