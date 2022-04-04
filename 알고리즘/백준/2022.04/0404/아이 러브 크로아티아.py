K = int(input()) - 1
N = int(input())
quizs = []
for n in range(N):
    tmp = input().split()
    tmp[0] = int(tmp[0])
    quizs.append(tmp)
# print(quizs)
time = 60*3 + 30
# print(time)
i = 0
while True:
    now = quizs[i]
    # print(now, time, K, i)
    if time < now[0]:
        break
    if now[1] == 'T':
        time -= now[0]
        K = (K+1)%8
        i += 1
    elif now[1] == 'N':
        time -= now[0]
        i += 1  
    elif now[1] == 'P':
        time -= now[0]
        i += 1
print(K+1)