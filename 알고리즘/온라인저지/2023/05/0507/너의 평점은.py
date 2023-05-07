grade_to_score = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

time_sum = 0
result = 0
while True:
    try:
        subject, time, grade = input().split()
        if grade == 'P':
            continue
        time = int(time[0])
        time_sum += time
        result += time*grade_to_score[grade]
    except EOFError:
        break
print(f'{result/time_sum:.6f}')