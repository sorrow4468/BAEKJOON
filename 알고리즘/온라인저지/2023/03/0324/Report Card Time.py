grades = ['F']*60 + ['D']*7 + ['D+']*3 + ['C']*7 + ['C+']*3 + ['B']*7 + ['B+']*3 + ['A']*7 + ['A+']*4
for _ in range(int(input())):
    name, score = input().split()
    score = int(score)
    print(name, grades[score])