S, K, H = map(int, input().split())

OK_check = True

dictt = {
    S:'Soongsil',
    K:'Korea',
    H:'Hanyang',
}

if S+K+H >= 100:
    print('OK')
else:
    print(dictt[min(S,K,H)])
