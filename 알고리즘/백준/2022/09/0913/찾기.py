import sys

input = sys.stdin.readline

def get_pi(pattern):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
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
                result.append(i-j+1)
                result[0] += 1
                j = pi[j] # 다음 패턴 찾는 인덱싱 주의
            else:
                j += 1

S, P = input().rstrip(), input().rstrip()
pi = [0] * len(P)
result = [0]
KMP(S, P)
for r in result: print(r)

# https://www.acmicpc.net/problem/1786