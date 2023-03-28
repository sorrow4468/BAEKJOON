K = int(input())
D1, D2 = map(int, input().split())
print(f'{K**2 - ((D1-D2)/2)**2:.6f}')