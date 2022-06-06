N = int(input())
F = int(input())
tmp = ((N//100)*100)
if tmp%F:
    print((str((tmp//F)*F + F)+'0')[-3:-1])
else:
    print((str((tmp//F)*F)+'0')[-3:-1])
