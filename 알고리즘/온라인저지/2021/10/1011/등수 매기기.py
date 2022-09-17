N = int(input())

students = []

for n in range(N):
    students.append(int(input()))

students.sort()

grades = list(range(1, N+1))

for i in range(N):
    students[i] = abs(students[i] - grades[i])

print(sum(students))