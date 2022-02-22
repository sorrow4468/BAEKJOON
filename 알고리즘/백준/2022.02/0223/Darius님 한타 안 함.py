K, D, A = map(int, input().split('/'))

is_Darius = 'gosu'

if K + A < D or D == 0:
    is_Darius = 'hasu'

print(is_Darius)