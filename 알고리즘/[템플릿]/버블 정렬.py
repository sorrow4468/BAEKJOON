arr = [55, 7, 42, 78, 12]
for i in range(len(arr)-1, 0, -1):
    for j in range(i):
        print(i, j)
        if arr[j] > arr[j+1]:
            print(f'{arr[j]}가 {arr[j+1]}보다 크므로, {arr[j]}와 {arr[j+1]}의 자리를 변경')
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
