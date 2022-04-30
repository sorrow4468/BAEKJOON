"""
1 2 3 4
4 1 3 2
4 3
1 2

4 4 3 4
3 4 4 4
4 4
3 4

4 7 3 9
3 4 7 9
9 3 7 4

"""
A, B = map(int, sorted(list(map(int, input().split())))[:3:2])
print(A*B)