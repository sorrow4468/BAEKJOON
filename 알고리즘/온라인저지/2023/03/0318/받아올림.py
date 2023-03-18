while True:
    A, B = input().split()
    if A == '0' and B == '0': break
    A = '00000000000000'+A
    B = '00000000000000'+B
    arr = []
    A = list(A)[::-1]
    B = list(B)[::-1]
    for i in range(10):
        a, b = map(int, (A[i], B[i]))
        C = a+b
        if C:
            arr.append(C)
    arr.append(0)
    result = 0
    for i in range(len(arr)):
        a = arr[i]
        if a>=10:
            result += 1
            arr[i+1] += 1
    print(result)