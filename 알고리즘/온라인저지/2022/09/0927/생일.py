import sys

input = sys.stdin.readline

students = []
for _ in [0]*int(input().rstrip()):
    student = input().rstrip().split()
    name = [student[0]]
    birthday = list(map(int, student[1:]))
    students.append(name+birthday)
students.sort(key=lambda x:(x[3], x[2], x[1]))
print(students[-1][0])
print(students[0][0])