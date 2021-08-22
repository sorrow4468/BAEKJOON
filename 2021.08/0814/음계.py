notes = list(map(int, input().split()))
ascending = 0
descending = 0
for i in range(1, len(notes)):
    if notes[i-1] < notes[i]:
        ascending += 1
    else:
        descending += 1
if ascending != 0 and descending != 0:
    print('mixed')
else:
    if ascending:
        print('ascending')
    else:
        print('descending')