A, B = input(), input()
arr1, arr2 = [0]*26, [0]*26
for a in A:
    i = ord(a)-97
    arr1[i] += 1
for b in B:
    i = ord(b)-97
    arr2[i] += 1
result = 0
for i in range(26):
    result += abs(arr1[i]-arr2[i])
print(result)

"""
같은 알파벳이 같은 개수만큼 있어야 함
문제에서는 알파벳을 새로 추가하지는 않고
불필요할 경우 제거하면서
애너그램을 만듬
몇개를 제거해야 하는가
"""