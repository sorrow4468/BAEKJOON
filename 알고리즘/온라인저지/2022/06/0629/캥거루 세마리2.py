while True:
    try:
        A, B, C = map(int, input().split())
        result = 0
        al = abs(A-B)
        cl = abs(B-C)
        if al <= cl:
            result += C - (B+1)
        elif al > cl:
            result += (B-1) - A
        print(result)
    except:
        break