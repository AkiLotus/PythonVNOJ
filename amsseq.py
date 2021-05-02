n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

dp = [float("-inf") for _ in a]
dp[0] = 0

for i in range(1, len(a)):
	for j in range(max(i-k, 0), i):
		dp[i] = max(dp[i], dp[j] + a[i])

print(dp)
print(max(dp))
