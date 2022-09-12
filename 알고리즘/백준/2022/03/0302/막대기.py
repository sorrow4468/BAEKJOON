N = int(input())

sticks = []

for n in range(N):
    sticks.append(int(input()))

TH = 0 # Top Height

cnt = 0

for s in sticks[::-1]:
    if s > TH:
        TH = s
        cnt += 1

print(cnt)