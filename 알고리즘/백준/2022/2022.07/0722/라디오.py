A, B = map(int, input().split())
N = int(input())
F = [] # favorite
R = A # radio
for n in range(N):
    F.append(int(input()))
minn = abs(B-R)
for f in F:
    tmp = abs(B-f)
    if tmp < minn: 
        minn = tmp
        R = f
result = 0
if R != A: # 즐겨찾기를 한 번 누름
    result += 1
result += abs(B-R)
print(result)