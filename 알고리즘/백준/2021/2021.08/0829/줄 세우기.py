import sys

student_count = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
result = []
for i in range(len(numbers)):
    result.insert(numbers[i], i+1)
result.reverse()
print(*result)
