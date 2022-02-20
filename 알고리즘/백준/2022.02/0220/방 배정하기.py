A, B, C, N = map(int, input().split())

found_ans = False

for a in range(N//A + 1):
    if found_ans:
        break
    for b in range(N//B + 1):
        if found_ans:
            break
        for c in range(N//C + 1):
            tmp = N-(a*A + b*B + c*C)
            if not tmp:
                found_ans = True
                break

print(1 if found_ans else 0)