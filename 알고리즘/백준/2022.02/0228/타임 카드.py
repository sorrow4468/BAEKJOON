for _ in range(3):
    AH, AM, AS, BH, BM, BS = map(int, input().split())

    BH -= 1 + AH
    BM += 59 - AM
    BS += 60 - AS
    
    if BS >= 60:
        BM += 1
        BS -= 60

    if BM >= 60:
        BH += 1
        BM -= 60

    print(BH, BM, BS)