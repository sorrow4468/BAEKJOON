N = input()
tmp = 3-len(N)%3
if tmp != 3: N = '0'*tmp + N
for i in range(0, len(N), 3):
    S = N[i:i+3] # section
    S = S[::-1]
    tmp = 0
    for j in range(len(S)):
        tmp += int(S[j])*(2**j)
    print(tmp, end='')