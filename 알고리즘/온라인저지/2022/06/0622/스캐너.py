R, C, ZR, ZC = map(int, input().split())
result = []
for r in range(R):
    tmp = input()
    a = ''
    for t in tmp:
        for zc in range(ZC):
            a = a + t
    for zr in range(ZR):
        result.append(a)
for r in result:
    print(r)