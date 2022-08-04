N = input()
M = len(N)//2 # middle
F, B = N[:M], N[M:] # front, back
F_int, B_int = 0, 0
for f in F: F_int += int(f)
for b in B: B_int += int(b)
print('LUCKY' if F_int == B_int else 'READY')