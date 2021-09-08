import sys
def input():
    return sys.stdin.readline()

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    cnt = 0
    end = True
    while end:
        if docs[M] != max(docs):
            if docs[0] != max(docs):
                docs.append(docs.pop(0))
                M -= 1
                if M < 0:
                    M += N
            else: # docs[0] == max(docs)
                docs.pop(0)
                cnt += 1
                N -= 1
                M -= 1    
        else: # docs[M] == max(docs)
            if M != 0:
                if docs[0] == docs[M]:
                    docs.pop(0)
                    cnt += 1
                    M -= 1
                else: # docs[0] != docs[M]
                    docs.pop(0)
                    M -= 1
            else: # M == 0
                cnt += 1
                end = False
                break
    print(cnt)
