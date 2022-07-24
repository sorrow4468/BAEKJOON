N, K = map(int, input().split())
buckets = list(range(1, K+1))
buckets.sort(reverse=True)
result = 0
if N < sum(buckets):
    result = -1
else:
    idx = 0
    for i in range(N-sum(buckets)):
        buckets[idx] += 1
        idx = (idx+1)%K
    result = max(buckets) - min(buckets)
print(result)