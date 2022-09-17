# stroke
S = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
name1 = input()
name2 = input()
for n in name1:
    tmp = ord(n)-65
arr = []
for i in range(len(name1)):
    arr.append(S[ord(name1[i])-65])
    arr.append(S[ord(name2[i])-65])
for i in range(len(arr)-2):
    tmp = [0] * (len(arr)-1)
    for j in range(len(arr)-1):
        tmp[j] = (arr[j]+arr[j+1])%10
    arr = tmp
for a in arr: print(a, end='')