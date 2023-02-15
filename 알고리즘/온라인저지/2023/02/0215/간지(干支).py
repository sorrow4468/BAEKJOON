year = int(input())
tmp = 'IJKLABCDEFGH'
print(tmp[year%12], (year+6)%10, sep='')