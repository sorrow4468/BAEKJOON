dp = [0] * 26

S = input()

for s in S:
    dp[ord(s)-97] += 1

print(*dp)    