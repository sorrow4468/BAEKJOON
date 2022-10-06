import sys

input = sys.stdin.readline
mod = int(1e9)+7

def multiply(matrix1, matrix2): # 행렬 곱셈
    output = []
    for i in range(2):
        output.append([])
        for j in range(2):
            tmp = 0
            for k in range(2):
                tmp += matrix1[i][k] * matrix2[k][j]
            output[i].append(tmp%mod)
    return output

def power(matrix, n): # 거듭제곱 분할정복
    if n == 1: return matrix
    tmp = power(matrix, n//2)
    if n%2 == 0:
        return multiply(tmp, tmp)
    else:
        return multiply(multiply(tmp, tmp), matrix)

N = int(input().rstrip())
matrix = [[1, 1], [1, 0]] # 피보나치 행렬 거듭제곱 일반항
print(power(matrix, N)[0][1])

"""
피보나치 일반항을, 행렬의 거듭제곱으로 변환할 줄 알아야 하고
행렬의 거듭제곱을 할 줄 알아야 하고
거듭제곱을 분할정복으로 할 줄 알아야 풀 수 있는 문제이다
2022-10-08기준, 가장 빠른 속도로 피보나치를 구할 수 있는 코드이다

<참고한 링크>
참고한 코드 원문
https://ca.ramel.be/50

백준 피보나치 블로그글
https://www.acmicpc.net/blog/view/28

피보나치가 [1, 1],[1, 0]의 거듭제곱이 되는 과정
https://www.youtube.com/watch?v=uX2IsIykLJc
"""

# https://www.acmicpc.net/problem/11444