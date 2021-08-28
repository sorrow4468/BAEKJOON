import sys

def arithmetic_sequence(N):
    if N < 100:
        return N
    else:
        cnt = 0
        for n in range(100, N+1):
            a, b, c = n//100, (n-(n//100)*100)//10, n%10
            for k in range(6):
                if (a+k == b and b+k == c and a+(k*2) == c) or (c+k == b and b+k == a and c+(k*2) == a):
                    cnt += 1
        return 99 + cnt

N = int(sys.stdin.readline())
print(arithmetic_sequence(N))