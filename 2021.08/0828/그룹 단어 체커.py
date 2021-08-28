import sys

T = int(sys.stdin.readline())
cnt = 0
for tc in range(T):
    word = sys.stdin.readline()
    i = 0
    char = []
    for i in range(len(word)):
        if word[i] not in char:
            char.append(word[i])
        else:
            if word[i] == word[i-1]:
                pass
            else:
                cnt -= 1
                break
    cnt += 1
print(cnt)
        