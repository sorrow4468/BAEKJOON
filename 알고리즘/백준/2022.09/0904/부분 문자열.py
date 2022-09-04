def get_pi(pattern):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

def KMP(string, pattern):
    get_pi(pattern)
    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != pattern[j]:
            j = pi[j-1]
        if string[i] == pattern[j]:
            if j == len(pattern)-1:
                return True
            else:
                j += 1
    return False

S, P = input(), input()
pi = [0] * len(P)
if KMP(S, P): print('1')
else: print('0')