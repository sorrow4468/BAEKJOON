tmp = input().split()

result = list(set(tmp))

result.sort()

for r in result:
    if r == result[-1]:
        print(r, end='')
        print()
        break

    print(r, end=',')