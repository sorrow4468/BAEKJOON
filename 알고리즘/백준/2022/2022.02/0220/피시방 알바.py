N = int(input())

guests = list(map(int, input().split()))

pcs = [False] * 101

reject = 0

for g in guests:
    if pcs[g]:
        reject += 1
        continue

    pcs[g] = True

print(reject)
