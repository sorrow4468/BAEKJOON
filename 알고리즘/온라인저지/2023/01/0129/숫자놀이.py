M, N = map(int, input().split())
arr = []
num_to_en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num_list = list(range(M, N+1))
for num in num_list:
    tmp = ''
    for i in str(num):
        tmp += num_to_en[int(i)]
    translated = [tmp, num]
    arr.append(translated)
arr.sort(key=lambda x:x[0])
cnt = 0
for a in arr: 
    print(a[1], end=' ')
    cnt = (cnt+1)%10
    if cnt == 0: print()
