import sys

print(dir(list))

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

pokemon_by_key = {}

for i in range(1, N+1):
    pokemon_by_key.update({i:input()})

key_by_pokemon = {v:k for k,v in pokemon_by_key.items()}

for i in range(M):
    quiz = input()
    try:
        print(pokemon_by_key.get(int(quiz)))
    except:
        print(key_by_pokemon.get(quiz))

