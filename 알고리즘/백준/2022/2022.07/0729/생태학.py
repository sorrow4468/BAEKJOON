import sys

input = sys.stdin.readline

dct = dict() # tree dict
lst = [] # tree list
cnt = 0
while True:
    tree = input().rstrip() # EOFerror
    if not tree: break
    if tree not in lst: lst.append(tree)
    try: dct[tree] += 1
    except: dct[tree] = 1
    cnt += 1
lst.sort()
for l in lst: print(f'{l} {dct[l]/cnt*100:.4f}')