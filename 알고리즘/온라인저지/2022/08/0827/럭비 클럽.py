result = ['Senior', 'Junior']
while True:
    tmp = input()
    if tmp == '# 0 0': break
    M = tmp.split()
    print(M[0], end=' ')
    if int(M[1]) > 17 or int(M[2]) >= 80:
        print(result[0])
    else:
        print(result[1])