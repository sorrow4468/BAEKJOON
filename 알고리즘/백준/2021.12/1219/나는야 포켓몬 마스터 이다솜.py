import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

pokemon = ['' for _ in range(N+1)]

for i in range(1, N+1):
    pokemon[i] = input()

for i in range(M):
    quiz = input()
    try:
        print(pokemon[int(quiz)])
    except:
        print(pokemon.index(quiz))