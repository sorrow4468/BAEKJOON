scores = list(map(int, input().split()))
hongik = int(input())
rank = scores.index(hongik)+1
if 1<=rank<6: result = 'A+'
elif 6<=rank<16: result = 'A0'
elif 16<=rank<31: result = 'B+'
elif 31<=rank<36: result = 'B0'
elif 36<=rank<46: result = 'C+'
elif 46<=rank<49: result = 'C0'
else: result = 'F'
print(result)