def palindrome(arr): # 팰린드롬을 찾아서 result에 추가하는 함수
    for i in range(N):
        for j in range(N-M+1):
            if not M%2:
                if arr[i][j:j+M//2] == arr[i][j+M:j+M//2-1:-1]:
                    result.append(arr[i][j:j+M])
                    break
            else:
                if arr[i][j:j+M//2] == arr[i][j+M:j+M//2:-1]:
                    result.append(arr[i][j:j+M])
                    break    


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = tuple(input() for _ in range(N))

    result = []
    # 가로
    palindrome(arr)
    
    # 세로 : 배열을 90도 뒤집어서 똑같은 코드 실행
    arr = list(arr)

    tmp = ['' for _ in range(N)]
    
    for a in arr:
        for i in range(N):
            tmp[i] = tmp[i] + a[i]
    
    palindrome(tmp)

    print('#{} {}'.format(t, *result))