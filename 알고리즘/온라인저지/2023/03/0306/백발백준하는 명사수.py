A, B, C = map(int, input().split())
D, E, F = map(int, input().split())
tmp = ((A-D)**2 + (B-E)**2) ** 0.5
print('YES' if tmp < C+F else 'NO')