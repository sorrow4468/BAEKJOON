result = 0
for i in range(int(input())):
    N = input()
    N, P = int(N[:len(N)-1]), int(N[-1])
    result += N**P
print(result)