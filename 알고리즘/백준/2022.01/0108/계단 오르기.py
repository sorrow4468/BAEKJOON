N = int(input())

stairs = []

for n in range(N):
    stairs.append(int(input()))

N -= 1

result = stairs[N]

while N >= 2:
    if stairs[N-1] >= stairs[N-2]:
        result += stairs[N-1]
        N -= 1
    else:
        result += stairs[N-2]
        N -= 2
    
if N == 1:
    result += stairs[N-1]

print(result)