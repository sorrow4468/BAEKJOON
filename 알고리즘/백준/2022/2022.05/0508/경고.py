from datetime import datetime

a = input()
b = input()
time_1 = datetime.strptime(a,"%H:%M:%S")
time_2 = datetime.strptime(b,"%H:%M:%S")
day_over = False
time_interval = time_2 - time_1
if str(time_interval)[0] == '-':
    day_over = True
if a == b: # 문제를 잘 읽자
    print('24:00:00')
elif day_over:
    if len(str(time_interval)) == 16:
        print(str(time_interval)[8:])
    else:
        print('0'+str(time_interval)[8:])
else:    
    if len(str(time_interval)) == 16:
        print(str(time_interval))
    else:
        print('0'+str(time_interval))