jh = input()
hospital = input()

for i in range(max(len(jh), len(hospital))):
    if hospital[i] == 'h':
        print('go')
        break
    elif jh[i] == 'h':
        print('no')
        break

