from math import gcd

a, b = map(int, input().split())
friendly = [False for _ in range(100000)]

for x in range(10, 100000):
	if friendly[x]: continue
	rev_x = int(str(x)[::-1])
	if gcd(rev_x, x) == 1:
		friendly[x] = True
		friendly[rev_x] = True

ans = 0
for x in range(a, b+1):
	ans += friendly[x]
print(ans)
