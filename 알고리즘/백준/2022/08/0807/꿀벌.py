import sys

input = sys.stdin.readline

T = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']
B = {t:0 for t in T}
cnt = 0
while True:
    I = input().rstrip().split()
    if not I: break
    for i in I:
        cnt += 1
        try: B[i] += 1
        except: pass
for t in T: print(f'{t} {B[t]} {B[t]/cnt:.2f}')
print(f'Total {cnt} 1.00')