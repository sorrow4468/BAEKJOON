A, B = map(int, input().split())
C, D = A-1, B-1
print(abs(C%4 - D%4) + abs(C//4 - D//4))