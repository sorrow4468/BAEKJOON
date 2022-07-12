FBI = False
result = []
for i in range(1, 6):
    agent = input()
    for j in range(len(agent)-2):
        tmp = agent[j:j+3]
        # print(tmp, i)
        if tmp == 'FBI':
            result.append(i)
            if not FBI:
                FBI = True
            break
if FBI:
    print(*result)
else:
    print('HE GOT AWAY!')