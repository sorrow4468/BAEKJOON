for i in range(int(input())):
    N, M = map(int, input().split())
    A = M-N+1
    B = A//2
    result = (N+M)*B
    if A%2:
        result += (N+M)//2
    print(f'Scenario #{i+1}:\n{result}\n')