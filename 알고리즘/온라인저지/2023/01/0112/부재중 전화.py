N, L, D = map(int, input().split())
song_len_max = N*L + (N-1)*5
ring_len_max = (song_len_max//D + 2)*D
arr1 = [0]*ring_len_max
arr2 = [0]*ring_len_max
i = 0
for n in range(N):
    for l in range(L):
        arr1[i] = 1
        i += 1
    i += 5
i = 0
while i < ring_len_max:
    arr2[i] += 1
    i += D
for i in range(ring_len_max):
    if not arr1[i] and arr2[i]:
        print(i)
        break