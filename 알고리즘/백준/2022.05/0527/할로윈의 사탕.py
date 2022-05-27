T = int(input())
for t in range(T):
    C, V = map(int, input().split())
    A, B = C//V, C%V
    print(f'You get {A} piece(s) and your dad gets {B} piece(s).')