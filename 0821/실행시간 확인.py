import timeit

start_time = timeit.default_timer()
arr = list(range(1000, -1, -1))

# 버블정렬
for i in range(len(arr)-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

# # sort()
# arr.sort()

end_time = timeit.default_timer()
print(f'{end_time-start_time:.5f}')