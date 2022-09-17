A, B = input().split()

A5 = A.replace('6', '5')
A6 = A.replace('5', '6')
B5 = B.replace('6', '5')
B6 = B.replace('5', '6')

print(int(A5) + int(B5), int(A6) + int(B6))