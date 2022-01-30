n, m = map(int, input().split())

for i in range(n-1):
    if i >= n-m+1:
        print('{} {}'.format(n-m, i+1))
        continue
    
    print(i, end=' ')
    print(i+1)
