N = int(input())
print(sum(list(map(abs, list(map(int, input().split()))))) + sum(list(map(abs, list(map(int, input().split()))))))