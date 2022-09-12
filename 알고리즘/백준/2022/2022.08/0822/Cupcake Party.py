B = [int(input()) for _ in range(2)] # box
C = B[0]*8 + B[1]*3 # cake
print(C-28 if C-28>0 else 0)